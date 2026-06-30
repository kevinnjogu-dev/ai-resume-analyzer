"""
Resume scoring functions.

Provides keyword matching and ATS-style scoring.
"""


def keyword_match_score(resume, job_description):
    """
    Calculates keyword overlap between resume and job description.
    """

    resume_words = set(resume.lower().split())
    job_words = set(job_description.lower().split())

    if not job_words:
        return 0

    matches = resume_words.intersection(job_words)

    return round((len(matches) / len(job_words)) * 100, 2)


def skill_match_score(resume, skills):
    """
    Measures how many relevant skills appear in the resume.
    """

    resume_text = resume.lower()

    matched_skills = [
        skill for skill in skills
        if skill.lower() in resume_text
    ]

    if not skills:
        return 0

    return round((len(matched_skills) / len(skills)) * 100, 2)


def overall_score(keyword_score, skill_score):
    """
    Generates a weighted ATS score.
    """

    score = (
        keyword_score * 0.5 +
        skill_score * 0.5
    )

    return round(score, 2)


def resume_strength(score):
    """
    Converts score into a hiring assessment.
    """

    if score >= 80:
        return "Strong Match"
    elif score >= 60:
        return "Moderate Match"
    else:
        return "Weak Match"