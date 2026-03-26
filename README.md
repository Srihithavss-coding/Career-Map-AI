# 🪐 Universal Career Architect AI
**An Intelligent Heuristic Engine for Multi-Stratum Career Mapping**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](https://career-map-ai-imfqqxxvvpvvhzj7ebnsps.streamlit.app/)

## 🔗 Live Deployment
**Interactive Interface:** [Launch Career Architect](https://career-map-ai-imfqqxxvvpvvhzj7ebnsps.streamlit.app/)

---

## 🛠️ Project Thesis
The **Universal Career Architect** is a sophisticated decision-support system designed to solve the "Domain Alignment Problem." Traditional career tools fail by using static taxonomies. This project utilizes **Large Language Models (LLMs)** and **Prompt Engineering frameworks** to dynamically synthesize roadmaps for users across the entire socio-economic spectrum—from specialized post-graduates to vocational aspirants with no formal schooling.

---

## 🧠 Technical Deep-Dive & Engineering Rigor

### 1. Prompt Engineering Architecture (TCREF Framework)
The core intelligence relies on a multi-layered **TCREF (Task, Context, Role, Entities, Format)** system instruction. This ensures the model maintains a high **Signal-to-Noise Ratio**:
* **Dynamic Branching Logic:** The engine performs a real-time "Education-Status Check." If the user is 12th Science, it prioritizes **STEM High-ROI** paths (e.g., Aerospace, Quantum Computing). If the user lacks formal schooling, it pivots to **Skill-to-Market** vocational strategies (e.g., Precision Mechanics, Logistics).
* **Semantic Mapping:** We implemented logic to prevent "Hobby-Looping." Instead of treating casual interests as end-goals, the AI treats them as **Niche Indicators**. 
    * *Example:* Identifying "Physics + Space History" as a trajectory for **Archeoastronomy** or **Planetary Data Science**.

### 2. Full-Stack AI Integration
* **Engine:** `Gemini-2.5-Flash` via Google GenAI SDK.
* **State Management:** Utilized `streamlit.session_state` to maintain a persistent **Conversation Buffer**, allowing the model to cross-reference early educational inputs during the final synthesis phase.
* **Resiliency Layer:** Developed a custom `safe_generate` wrapper with **Exponential Backoff** to mitigate `429 RESOURCE_EXHAUSTED` errors. This ensures system availability during high-traffic API bursts.

### 3. Data Flow & UI/UX
* **Frontend:** Built with Streamlit for a reactive, low-latency web experience.
* **Deployment:** CI/CD integration via GitHub to Streamlit Cloud with encrypted **Secret Management** for API security.

---

## 📊 Performance Analysis
| Feature | Implementation | Impact |
| :--- | :--- | :--- |
| **Persona Switching** | TCREF Conditional Logic | 100% adaptation to User Education level. |
| **Error Handling** | Try-Except Retry Loop | Zero-crash state during Rate-Limiting. |
| **Data Extraction** | Entity Recognition | Maps raw interests to 5-year ROI targets. |

---

## 🏗️ Setup & Installation
```bash
# Clone the repository
git clone [https://github.com/Srihithavss-coding/Career-Map-AI.git](https://github.com/Srihithavss-coding/Career-Map-AI.git)

# Install dependencies
pip install -r requirements.txt

# Launch the engine
streamlit run streamlit_app.py