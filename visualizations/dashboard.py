"""
Resume Analysis Dashboard

Creates visualization for ATS scoring results.
"""

import json
import matplotlib.pyplot as plt


with open("data/analysis_results.json", "r") as file:
    results = json.load(file)


categories = [
    "Keyword Match",
    "Skill Match",
    "Overall Score"
]

scores = [
    results["keyword_match_score"],
    results["skill_match_score"],
    results["overall_score"]
]


plt.figure(figsize=(7, 4))

plt.bar(categories, scores)

plt.title("AI Resume Analyzer - ATS Score Report")
plt.ylabel("Score")
plt.ylim(0, 100)

for index, score in enumerate(scores):
    plt.text(
        index,
        score + 2,
        f"{score}%",
        ha="center"
    )


plt.savefig(
    "visualizations/resume_score.png",
    bbox_inches="tight"
)

print("ATS dashboard created successfully.")