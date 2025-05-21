# 📄 JobFit GPT – Resume vs Job Description Analyzer

An AI-powered Streamlit web app that analyzes how well a resume matches a job description. Combines keyword similarity (TF-IDF) with GPT-3.5 to deliver smart match scoring, skill gap detection, and tailored resume improvement suggestions.

---

## 🚀 Features

-  Upload a **resume (PDF)** and paste a **job description**
-  Calculates a **match score** using TF-IDF and cosine similarity
-  Displays matched & missing skills
-  Uses **OpenAI GPT-3.5** to suggest resume bullet improvements
-  Deployed via **Streamlit Cloud** with secure `.env` key handling

---

## 🛠 Tech Stack

- Python, Streamlit
- TF-IDF (scikit-learn)
- GPT-3.5 via OpenAI API
- PyMuPDF (resume parsing)
- `python-dotenv` for environment variables

---

## 📦 Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/Sbatchu1901/jobfit-gpt-app.git
cd jobfit-gpt-app
