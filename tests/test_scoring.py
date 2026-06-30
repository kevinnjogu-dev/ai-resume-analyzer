from src.scoring import keyword_match_score, resume_strength


def test_keyword_match():
    resume = "Python Machine Learning Git"
    job = "Python Git SQL"

    score = keyword_match_score(resume, job)

    assert score > 0


def test_resume_strength():
    assert resume_strength(90) == "Strong Match"
    assert resume_strength(70) == "Moderate Match"
    assert resume_strength(40) == "Weak Match"