import streamlit as st
import time
from google import genai
from google.genai import errors

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Career Architect", page_icon="🚀")
st.title("🚀 Universal Career Architect")
st.caption("TCREF-Optimized Professional Roadmap Generator")

# --- API SETUP ---
# In a real app, use st.secrets for the API key
# This pulls the key from Streamlit's secure settings instead of the code
API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=API_KEY)
MODEL_NAME = "gemini-2.5-flash"

# --- TCREF SYSTEM INSTRUCTION ---
TCREF_MASTER_INSTRUCTION = """
ROLE: Universal Career & Livelihood Architect.
CONTEXT: User levels range from 10th/12th/Grad to No Formal Education.
TASK: Identify a high-ROI career path. 
LOGIC: 
- Students: Prioritize Science/Math/History logic + Entrance Exams.
- No Education: Prioritize 'Skill-to-Market' (Repairs, Stitching, driving).
- Grads: Prioritize 'Bridge' skills to new industries.
RULE: Ask ONLY one short question at a time. Total turns: 5.
"""

# --- SESSION STATE INITIALIZATION ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "model", "parts": [{"text": "Welcome! To build your professional blueprint, what is your current educational status (e.g., 10th, 12th, Graduate, or No Formal Education)?"}]}
    ]

# --- CHAT INTERFACE ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["parts"][0]["text"])

# --- INPUT HANDLING ---
if prompt := st.chat_input("Type your response here..."):
    # 1. Display User Message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "parts": [{"text": prompt}]})

    # 2. Check Turn Count (Limit to 5 turns total)
    turn_count = len([m for m in st.session_state.messages if m["role"] == "user"])

    with st.chat_message("model"):
        with st.spinner("Architect is thinking..."):
            try:
                if turn_count < 5:
                    # Regular Interview Turn
                    response = client.models.generate_content(
                        model=MODEL_NAME,
                        config={"system_instruction": TCREF_MASTER_INSTRUCTION, "temperature": 0.4},
                        contents=st.session_state.messages
                    )
                    ai_text = response.text
                else:
                    # Final Blueprint Turn
                    st.info("✨ Limit reached. Synthesizing your 5-Year Blueprint...")
                    blueprint_prompt = "Generate a professional 5-year academic and professional roadmap based on this chat. Use tables and bold headers."
                    response = client.models.generate_content(
                        model=MODEL_NAME,
                        config={"system_instruction": blueprint_prompt, "temperature": 0.2},
                        contents=st.session_state.messages
                    )
                    ai_text = "### 🏁 YOUR STRATEGIC BLUEPRINT\n" + response.text

                st.markdown(ai_text)
                st.session_state.messages.append({"role": "model", "parts": [{"text": ai_text}]})

            except errors.ClientError as e:
                if "429" in str(e):
                    st.error("⏳ API Quota reached. Please wait 60 seconds and try again.")
                else:
                    st.error(f"An error occurred: {e}")