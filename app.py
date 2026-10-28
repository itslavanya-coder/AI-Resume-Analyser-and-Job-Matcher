import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer and Job Matcher")
st.write("Resume Skill Analysis and Job Matching")

skills = [
    "python", "pandas", "numpy",
    "machine learning", "sql",
    "matplotlib", "seaborn", "tensorflow"
]

job_skills = {
    "python", "pandas",
    "machine learning", "sql", "tensorflow"
}

resume_text = st.text_area(
    "Paste Your Resume Text",
    height=200
)

if st.button("Analyze Resume"):

    if not resume_text.strip():
        st.warning("Please enter your resume text.")

    else:
        resume_text = resume_text.lower()

        resume_skills = {
            skill for skill in skills
            if skill in resume_text
        }

        matched_skills = resume_skills.intersection(job_skills)
        missing_skills = job_skills - resume_skills

        match_percentage = (
            len(matched_skills) / len(job_skills)
        ) * 100

        st.subheader("Resume Skills")
        st.write(sorted(resume_skills))

        st.subheader("Job Required Skills")
        st.write(sorted(job_skills))

        st.subheader("Matched Skills")
        st.success(", ".join(sorted(matched_skills)) or "None")

        st.subheader("Missing Skills")
        st.warning(", ".join(sorted(missing_skills)) or "None")

        st.subheader("Job Match Percentage")
        st.metric("Job Match", f"{match_percentage:.2f}%")

        st.progress(match_percentage / 100)

        st.subheader("Resume vs Job Skill Match")

        fig, ax = plt.subplots()

        ax.bar(
            ["Matched", "Missing"],
            [len(matched_skills), len(missing_skills)]
        )

        ax.set_title("Resume vs Job Skill Match")
        ax.set_xlabel("Skills")
        ax.set_ylabel("Number of Skills")

        st.pyplot(fig)
        plt.close(fig)