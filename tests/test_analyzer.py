from src.analyzer import analyze


def test_resume_analysis():

    results = analyze(
        "data/sample_resume.txt",
        "data/sample_job_description.txt"
    )

    assert "keyword_match_score" in results
    assert "skill_match_score" in results
    assert "overall_score" in results
    assert "assessment" in results

    assert 0 <= results["overall_score"] <= 100