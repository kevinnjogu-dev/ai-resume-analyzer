"""
Utility functions for reading and writing files.
"""

import json


def load_text(filepath):
    """Load text from a file."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def save_json(data, filepath):
    """Save analysis results to JSON."""
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)