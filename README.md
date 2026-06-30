# AI Resume Analyzer

[![Python Tests](https://github.com/kevinnjogu-dev/ai-resume-analyzer/actions/workflows/python-tests.yml/badge.svg)](https://github.com/kevinnjogu-dev/ai-resume-analyzer/actions)

An AI-assisted resume analysis toolkit that evaluates resumes against job descriptions using ATS-style scoring, structured evaluation metrics, and automated analysis workflows.

This project demonstrates practical applications of **resume screening automation, prompt engineering concepts, structured scoring systems, and AI evaluation workflows**.

---

## Project Overview

Recruiters often review hundreds of resumes for a single position. This project simulates an Applicant Tracking System (ATS) workflow by analyzing a resume against a job description and generating a structured candidate assessment.

The analyzer evaluates resumes using:

* Keyword Match Score
* Skill Match Score
* Weighted Overall Score
* Candidate Match Assessment

The goal is to provide a transparent and explainable approach to resume evaluation.

---

## Features

* Resume and job description comparison
* ATS-style scoring system
* Keyword matching analysis
* Skill-based evaluation
* Weighted overall candidate score
* JSON-based analysis reports
* Visualization dashboard
* Modular Python architecture
* Automated testing with pytest
* Continuous integration using GitHub Actions

---

## How It Works

```text
Resume + Job Description
          |
          ↓
Text Processing
          |
          ↓
Keyword Matching
          |
          ↓
Skill Evaluation
          |
          ↓
Weighted ATS Score
          |
          ↓
Candidate Assessment
          |
          ↓
Visualization Report
```

---

## Example Output

```json
{
    "keyword_match_score": 40.0,
    "skill_match_score": 71.43,
    "overall_score": 55.72,
    "assessment": "Weak Match"
}
```

---

## Dashboard Preview

![ATS Resume Score](visualizations/resume_score.png)

---

## Repository Structure

```text
ai-resume-analyzer/

├── data/
├── docs/
├── examples/
├── notebooks/
├── prompts/
│
├── src/
│   ├── analyzer.py
│   ├── scoring.py
│   ├── utils.py
│   └── __init__.py
│
├── tests/
│   ├── test_scoring.py
│   └── test_analyzer.py
│
├── visualizations/
│   ├── dashboard.py
│   └── resume_score.png
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## Technologies

* Python
* Pytest
* Matplotlib
* JSON Data Processing
* Prompt Engineering Concepts
* ATS Evaluation Workflows

---

## Running the Project

### Analyze a Resume

```bash
python -m src.analyzer
```

### Generate Visualization

```bash
python visualizations/dashboard.py
```

### Run Tests

```bash
python -m pytest
```

---

## Testing

The project uses automated testing with pytest.

Current test coverage includes:

* Resume scoring logic
* ATS scoring calculations
* Resume analysis workflow

All tests run automatically through GitHub Actions.

---

## Future Improvements

Planned enhancements:

* PDF resume parsing
* Natural language processing
* Semantic similarity using embeddings
* LLM-generated resume feedback
* ATS optimization recommendations
* Interactive web dashboard

---

## Author

**Kevin Njogu**

AI Trainer | LLM Evaluator | Machine Learning Enthusiast
