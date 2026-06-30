"""
Utility functions for reading and writing files.
"""

import json
import pdfplumber


def load_text(filepath):
    """
    Load text from TXT or PDF files.
    """

    if filepath.endswith(".pdf"):

        text = ""

        with pdfplumber.open(filepath) as pdf:

            for page in pdf.pages:
                text += page.extract_text() or ""

        return text


    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def save_json(data, filepath):
    """
    Save analysis results to JSON.
    """

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)