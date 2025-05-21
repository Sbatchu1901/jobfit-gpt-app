# jd_matcher.py (TF-IDF Version)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def clean_text(text):
    return re.sub(r'\W+', ' ', text.lower())

def extract_keywords(text):
    return set(clean_text(text).split())

def compute_similarity(resume_text, job_desc):
    # Preprocess
    resume_text = clean_text(resume_text)
    job_desc = clean_text(job_desc)

    # Compute TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_desc])

    # Compute cosine similarity
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    # Keyword overlap
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(job_desc)

    matched = list(resume_keywords & jd_keywords)
    missing = list(jd_keywords - resume_keywords)

    return round(similarity_score * 100, 2), matched[:10], missing[:10]
