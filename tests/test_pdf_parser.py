from src.utils import load_text


def test_load_pdf():

    text = load_text("data/sample_resume.pdf")

    assert isinstance(text, str)
    assert len(text) > 0