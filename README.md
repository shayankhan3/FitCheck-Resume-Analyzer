# Fit - Resume Analyzer 📄🚀

An AI-powered Resume Analyzer built using **Streamlit**, **LangChain**, and **Groq (Llama-3.3-70b)**. This application extracts text from a PDF resume, compares it against a target job title, and acts as an expert HR Consultant to provide detailed insights.

## 🌟 Features
* **PDF Text Extraction:** Seamlessly reads and extracts text from uploaded PDF resumes using `pypdf`.
* **AI-Powered HR Insights:** Leverages Groq's ultra-fast `llama-3.3-70b-versatile` model.
* **Targeted Evaluation:** Analyzes the resume based on a specific Job Title provided by the user.
* **Detailed Breakdown:** Provides structured feedback covering:
  1. Strengths
  2. Weaknesses
  3. Areas of Improvement
  4. Overall Score (out of 10)
  5. Job Match Suitability

---

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/)
* **LLM Framework:** [LangChain](https://www.langchain.com/)
* **LLM Provider:** [Groq Cloud](https://console.groq.com/) (`llama-3.3-70b-versatile`)
* **PDF Parser:** `pypdf`
* **Environment Management:** `python-dotenv`

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### 1. Prerequisites
Make sure you have Python installed on your system. You will also need a **Groq API Key**. You can get it for free from [Groq Console](https://console.groq.com/).

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
