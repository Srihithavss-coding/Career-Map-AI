import os
import time
from google import genai
from google.genai import errors

# 1. INITIALIZATION
# Ensure your API key is correct and the model is set to 2.5-flash
client = genai.Client(api_key="AIzaSyCk4wBy1muhiUUi9RMWB7XN-_MXZzoj8H4")
MODEL_NAME = "gemini-2.5-flash" 

# 2. THE TCREF MASTER PROMPT
# This instruction set guides the AI to behave differently for every education level.
TCREF_MASTER_INSTRUCTION = """
### ROLE
You are a Universal Career & Livelihood Architect. Your goal is to move the user from their current state to a sustainable, high-value future.

### CONTEXT
The user could be a School Student, a Graduate, or an individual with NO formal education. You must detect this immediately and adapt your logic.

### TASK: CONDITIONAL LOGIC BY EDUCATION LEVEL
1. **FORMAL EDUCATION (10th, 12th, or Graduate):**
   - Focus: Knowledge Implementation.
   - 12th/10th: Prioritize academic streams and entrance exams (JEE, NEET, CLAT, etc.).
   - Graduates: Focus on job roles, specialized certifications, or Master's degrees.
   - If a hobby is mentioned (e.g., knots), translate it to a technical niche (e.g., Surgical Technology, Rigging, or Topology).

2. **NO FORMAL EDUCATION:**
   - Focus: Skill-to-Market.
   - Ask about physical or digital skills (e.g., repairs, driving, stitching, cooking).
   - Map interests to Vocational Training, the Gig Economy, or entrepreneurship.
   - Goal: Financial dignity and immediate employability.

### ENTITIES TO EXTRACT
Identify: [Education Level] -> [Primary Skill/Interest] -> [Marketable Value] -> [5-Year Target].

### FORMAT & RULES
- Ask ONLY ONE short, probing question per turn.
- Be highly professional for students/grads; be clear and encouraging for those without education.
- Never suggest a 'hobby' as a career unless it has a verified professional industry equivalent.
"""

def safe_generate(transcript, system_inst):
    """
    Handles API communication with built-in retry logic for Quota limits (429 errors).
    """
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            config={
                "system_instruction": system_inst, 
                "temperature": 0.4  # Lowered for more logical, less creative responses
            },
            contents=transcript
        )
        return response.text
    except errors.ClientError as e:
        if "429" in str(e):
            print("\n⏳ [QUOTA LIMIT] API is resting. Waiting 20 seconds to retry...", flush=True)
            time.sleep(21)
            return safe_generate(transcript, system_inst)
        else:
            print(f"\n❌ [ERROR] An unexpected issue occurred: {e}")
            raise e

def run_app():
    print("🚀 UNIVERSAL CAREER ARCHITECT INITIALIZED", flush=True)
    print("------------------------------------------", flush=True)
    
    transcript = []
    
    # Starting Question
    initial_message = "Welcome! To build your professional blueprint, what is your current educational status (e.g., 10th, 12th, Graduate, or No Formal Education)?"
    print(f"\n🤖 AI: {initial_message}", flush=True)
    transcript.append({"role": "model", "parts": [{"text": initial_message}]})

    # The 5-Turn Interview Loop
    for turn in range(4): # Loop for 4 follow-up questions
        user_input = input("You: ")
        transcript.append({"role": "user", "parts": [{"text": user_input}]})
        
        # Get AI response using TCREF logic
        ai_msg = safe_generate(transcript, TCREF_MASTER_INSTRUCTION)
        print(f"\n🤖 AI: {ai_msg}\n", flush=True)
        transcript.append({"role": "model", "parts": [{"text": ai_msg}]})

    # FINAL BLUEPRINT GENERATION
    print("\n✨ Turn limit reached. Synthesizing your Strategic Blueprint...", flush=True)
    
    final_blueprint_prompt = """
    Generate a comprehensive 5-Year Career Roadmap. 
    - For Students: Mention specific exams, college paths, and degrees.
    - For Graduates: Mention bridge skills and market entry.
    - For No Education: Mention vocational steps and income-generating skills.
    Use Bold headers and Markdown tables where applicable.
    """
    
    roadmap = safe_generate(transcript, final_blueprint_prompt)
    
    # Final Output Display
    print("\n" + "█"*60)
    print("          YOUR 5-YEAR PROFESSIONAL BLUEPRINT          ")
    print("█"*60 + "\n")
    print(roadmap)
    print("\n" + "█"*60)

if __name__ == "__main__":
    run_app()