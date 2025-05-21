from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()  # Load environment variables from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Fetch the key safely


def get_llm_feedback(resume_text, job_desc):
    prompt = f"""
You are an AI resume reviewer.
Compare the following resume and job description. Return:
1. Match score (0–100%)
2. Top 3 matched skills
3. Top 3 missing skills
4. 2 suggested bullet points to improve the resume

Resume:
{resume_text}

Job Description:
{job_desc}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content.strip()
