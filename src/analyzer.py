"""
AI Resume Analyzer

Compares a resume against a job description
using ATS-style scoring.
"""

from src.utils import load_text, save_json
from src.scoring import (
    keyword_match_score,
    skill_match_score,
    overall_score,
    resume_strength
)


def analyze(resume_file, job_file):

    resume = load_text(resume_file)
    job = load_text(job_file)

    skills = [
        "python",
        "machine learning",
        "data analysis",
        "sql",
        "git",
        "aws",
        "javascript"
    ]

    keyword_score = keyword_match_score(
        resume,
        job
    )

    skill_score = skill_match_score(
        resume,
        skills
    )

    final_score = overall_score(
        keyword_score,
        skill_score
    )

    results = {
        "keyword_match_score": keyword_score,
        "skill_match_score": skill_score,
        "overall_score": final_score,
        "assessment": resume_strength(final_score)
    }

    return results


if __name__ == "__main__":

    results = analyze(
        "data/sample_resume.txt",
        "data/sample_job_description.txt"
    )

    save_json(
        results,
        "data/analysis_results.json"
    )

    print("Resume analyzed successfully.")
    print(results)