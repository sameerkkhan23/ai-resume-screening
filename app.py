import os
import streamlit as st

from src.text_extraction import extract_text
from src.text_cleaning import clean_text
from src.similarity import calculate_similarity
from src.ranking import rank_resumes

st.set_page_config(page_title="AI Resume Screening System")
st.title("📄 AI Resume Screening System")

st.write("Upload resumes and paste job description to rank candidates.")

job_description = st.text_area("📌 Paste Job Description Here")

uploaded_files = st.file_uploader(
    "📤 Upload Resumes (PDF or DOCX)",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if st.button("🔍 Analyze Resumes"):
    if not job_description or not uploaded_files:
        st.warning("Please upload resumes and provide a job description.")
    else:
        resume_texts = []
        resume_names = []

        os.makedirs("data/resumes", exist_ok=True)

        for file in uploaded_files:
            file_path = f"data/resumes/{file.name}"
            with open(file_path, "wb") as f:
                f.write(file.getbuffer())

            text = extract_text(file_path)
            cleaned_text = clean_text(text)

            resume_texts.append(cleaned_text)
            resume_names.append(file.name)

        cleaned_jd = clean_text(job_description)

        scores = calculate_similarity(cleaned_jd, resume_texts)
        ranked_resumes = rank_resumes(resume_names, scores)

        
        st.subheader("📊 Resume Ranking Results")
        for idx, (name, score) in enumerate(ranked_resumes, start=1):
            match_percent = round(score * 100, 2)

        if match_percent < 5:
            st.write(f"**{idx}. {name}** → ❌ No significant match")
        else:
            st.write(f"**{idx}. {name}** → ✅ {match_percent}% match")
