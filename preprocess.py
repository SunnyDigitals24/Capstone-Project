"""Text preprocessing utilities for the capstone project."""

import re
import string


def normalize_whitespace(text: str) -> str:
    """Replace repeated whitespace with a single space."""
    if not isinstance(text, str):
        return ""
    return re.sub(r"\s+", " ", text).strip()


def remove_punctuation(text: str) -> str:
    """Remove punctuation from text."""
    if not isinstance(text, str):
        return ""
    return text.translate(str.maketrans("", "", string.punctuation))


def clean_text(text: str) -> str:
    """Basic text cleaning for article abstracts."""
    text = normalize_whitespace(text)
    return text


def tokenize(text: str) -> list[str]:
    """Tokenize text into lowercase words."""
    text = remove_punctuation(clean_text(text.lower()))
    return [word for word in text.split() if word]
