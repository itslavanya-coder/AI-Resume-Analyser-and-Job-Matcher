import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("AI Resume Analyzer Started!")

skills = [
    "Python",
    "Pandas",
    "NumPy",
    "Machine Learning",
    "SQL"
]

df = pd.DataFrame({
    "Skills": skills
})

print("\nResume Skills:")
print(df)