"""
Resume scoring functions.
"""


def keyword_match_score(resume, job_description):
    resume_words = set(resume.lower().split())
    job_words = set(job_description.lower().split())

    if not job_words:
        return 0

    matches = resume_words.intersection(job_words)
    return round((len(matches) / len(job_words)) * 100, 2)


def resume_strength(score):
    if score >= 80:
        return "Strong Match"
    elif score >= 60:
        return "Moderate Match"
    else:
        return "Weak Match"