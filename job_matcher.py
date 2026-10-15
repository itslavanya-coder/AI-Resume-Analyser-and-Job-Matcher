import os
import matplotlib.pyplot as plt

# Read resume
resume_path = os.path.join(os.path.dirname(__file__), "resume1.txt")

with open(resume_path, "r") as file:
    resume_text = file.read().lower()

# Skills
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

# Find resume skills
resume_skills = set()

for skill in skills:
    if skill in resume_text:
        resume_skills.add(skill)

# Job required skills
job_skills = {
    "python",
    "pandas",
    "machine learning",
    "sql",
    "tensorflow"
}

# Matched skills
matched_skills = resume_skills.intersection(job_skills)

# Missing skills
missing_skills = job_skills - resume_skills

# Match percentage
match_percentage = (
    len(matched_skills) / len(job_skills)
) * 100

# Terminal output
print("\nAI RESUME ANALYZER")
print("==================")

print("\nResume Skills:")
print(resume_skills)

print("\nJob Required Skills:")
print(job_skills)

print("\nMatched Skills:")
print(matched_skills)

print("\nMissing Skills:")
print(missing_skills)

print("\nJob Match Percentage:")
print(match_percentage, "%")

# Save result
with open("output/result.txt", "w") as file:
    file.write("AI RESUME ANALYZER\n")
    file.write("==================\n\n")

    file.write("Resume Skills:\n")
    file.write(str(resume_skills))

    file.write("\n\nJob Required Skills:\n")
    file.write(str(job_skills))

    file.write("\n\nMatched Skills:\n")
    file.write(str(matched_skills))

    file.write("\n\nMissing Skills:\n")
    file.write(str(missing_skills))

    file.write("\n\nJob Match Percentage:\n")
    file.write(str(match_percentage))
    file.write("%")

# Bar chart
labels = ["Matched", "Missing"]
values = [
    len(matched_skills),
    len(missing_skills)
]

plt.bar(labels, values)
plt.title("Resume vs Job Skill Match")
plt.xlabel("Skills")
plt.ylabel("Number of Skills")
plt.show()