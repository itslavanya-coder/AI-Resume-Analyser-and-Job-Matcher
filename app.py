import streamlit as st
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer and Job Matcher")
st.write("Resume Skill Analysis and Job Matching")

# Read original resume
resume_path = os.path.join(
    os.path.dirname(_file_), "resume1.txt"
)

with open(resume_path, "r", encoding="utf-8") as file:
    resume_text = file.read().lower()

# Original skills
skills = [
    "python",
    "pandas",
    "numpy",
    "machine learning",
    "sql",
    "matplotlib",
    "seaborn",
    "tensorflow"
]

resume_skills = {
    skill for skill in skills
    if skill in resume_text
}

job_skills = {
    "python",
    "pandas",
    "machine learning",
    "sql",
    "tensorflow"
}

matched_skills = resume_skills.intersection(job_skills)
missing_skills = job_skills - resume_skills

match_percentage = (
    len(matched_skills) / len(job_skills)
) * 100

# Display original results
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

# Original bar chart
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
