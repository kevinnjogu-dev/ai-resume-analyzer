"""
AI Resume Analyzer

Analyzes a resume against a job description.
Supports TXT and PDF resumes.
"""

import argparse

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

    keyword_score = keyword_match_score(resume, job)

    skills = [
        "python",
        "machine learning",
        "sql",
        "git",
        "aws"
    ]

    skill_score = skill_match_score(resume, skills)

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

    parser = argparse.ArgumentParser(
        description="AI Resume Analyzer"
    )

    parser.add_argument(
        "resume",
        help="Path to resume file (.txt or .pdf)"
    )

    parser.add_argument(
        "job",
        help="Path to job description file"
    )

    parser.add_argument(
        "--output",
        default="data/analysis_results.json",
        help="Output JSON file"
    )

    args = parser.parse_args()


    results = analyze(
        args.resume,
        args.job
    )

    save_json(
        results,
        args.output
    )


    print("Resume analyzed successfully.")
    print(results)