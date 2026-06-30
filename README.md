# AI Resume Analyzer

[![Python Tests](https://github.com/kevinnjogu-dev/ai-resume-analyzer/actions/workflows/python-tests.yml/badge.svg)](https://github.com/kevinnjogu-dev/ai-resume-analyzer/actions)

An AI-powered resume analysis toolkit designed to evaluate resumes against job descriptions using structured scoring, prompt engineering principles, and automated evaluation workflows.

This project demonstrates practical applications of **LLM evaluation, prompt engineering, resume screening automation, and AI-assisted candidate assessment**.

---

## Project Overview

Recruiters and hiring teams often process large volumes of resumes when searching for suitable candidates. This project simulates an intelligent resume evaluation workflow by analyzing resumes against job requirements and generating structured assessment results.

The analyzer evaluates resumes across multiple dimensions:

* Skills Match
* Experience Relevance
* Education Alignment
* Keyword Coverage
* Resume Clarity
* Overall Match Score

The goal is to demonstrate how AI systems can support structured candidate screening while maintaining transparent and explainable evaluation criteria.

---

## Features

* Resume and job description comparison
* Structured resume scoring system
* Keyword-based matching analysis
* JSON-based evaluation outputs
* Modular Python project architecture
* Evaluation result visualization
* Automated testing with pytest
* Prompt engineering workflow examples

---

## How It Works

The system follows a structured evaluation pipeline:

1. **Input Processing**

   * Resume data is collected and prepared for analysis.
   * Job descriptions are processed to identify relevant requirements.

2. **Resume Evaluation**

   * Resume content is analyzed against predefined evaluation criteria.
   * Scores are generated across different assessment categories.

3. **Results Generation**

   * Evaluation results are stored in structured JSON format.
   * Scores can be visualized for easier interpretation.

---

## Repository Structure

```
ai-resume-analyzer/
│
├── data/                 # Input and generated evaluation data
├── docs/                 # Project documentation
├── examples/             # Example inputs and outputs
├── notebooks/            # Exploratory analysis notebooks
├── prompts/              # Prompt engineering resources
├── src/                  # Core application logic
├── tests/                # Automated tests
├── visualizations/       # Generated charts and analysis visuals
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
* JSON Data Processing
* Matplotlib
* Prompt Engineering Concepts
* LLM Evaluation Workflows
* Markdown Documentation

---

## Testing

This project uses **pytest** for automated testing.

Run tests locally:

```bash
python -m pytest
```

Current tests validate:

* Resume scoring functionality
* Evaluation logic
* Core project components

---

## Future Improvements

Planned enhancements include:

* LLM-powered resume evaluation
* ATS compatibility scoring
* Semantic similarity analysis using embeddings
* PDF resume parsing
* Interactive resume analysis dashboard
* Advanced AI ranking recommendations

---

## Author

**Kevin Njogu**

AI Trainer | LLM Evaluator | Machine Learning Enthusiast

---

## License

This project is licensed under the MIT License.
