# jobfit_gpt_app/main_app.py

import streamlit as st
from resume_parser import extract_resume_text
from jd_matcher import compute_similarity, extract_keywords
from llm_feedback import get_llm_feedback

st.title("📄 JobFit GPT: Resume vs Job Description Analyzer")

# Upload resume file
uploaded_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])
cover_letter_file = st.file_uploader("📎 Optional: Upload a Cover Letter (PDF)", type=["pdf"])
job_description = st.text_area("📝 Paste the Job Description")

if uploaded_file and job_description and st.button("🔍 Analyze Resume"):
    resume_text = extract_resume_text(uploaded_file)

    if cover_letter_file:
        cover_text = extract_resume_text(cover_letter_file)  # Optional display

    with st.spinner("Analyzing..."):
        score, matched_skills, missing_skills = compute_similarity(resume_text, job_description)
        #feedback = get_gpt_feedback(resume_text, job_description)


    st.subheader(f"🎯 Match Score: {score}%")
    st.markdown(f"**✅ Matched Skills:** {', '.join(matched_skills)}")
    st.markdown(f"**❌ Missing Skills:** {', '.join(missing_skills)}")
    st.markdown("---")
    #st.subheader("🧠 GPT Resume Feedback")
    #st.write(feedback)

else:
    st.info("Please upload a resume and paste a job description to begin analysis.")


