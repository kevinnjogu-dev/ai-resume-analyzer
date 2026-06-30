import json
import matplotlib.pyplot as plt

with open("data/analysis_results.json", "r") as file:
    results = json.load(file)

score = results["keyword_match_score"]

plt.figure(figsize=(6, 4))
plt.bar(["Resume"], [score])
plt.title("Resume Match Score")
plt.ylabel("Score")
plt.ylim(0, 100)

plt.savefig("visualizations/resume_score.png")

print("Visualization saved successfully.")