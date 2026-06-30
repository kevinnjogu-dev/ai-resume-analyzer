"""
AI Resume Analyzer

Compares a resume against a job description.
"""

from src.utils import load_text, save_json
from src.scoring import keyword_match_score, resume_strength


def analyze(resume_file, job_file):
    resume = load_text(resume_file)
    job = load_text(job_file)

    score = keyword_match_score(resume, job)

    results = {
        "keyword_match_score": score,
        "assessment": resume_strength(score)
    }

    return results


if __name__ == "__main__":

    results = analyze(
        "data/sample_resume.txt",
        "data/sample_job_description.txt"
    )

    save_json(results, "data/analysis_results.json")

    print("Resume analyzed successfully.")
    print(results)