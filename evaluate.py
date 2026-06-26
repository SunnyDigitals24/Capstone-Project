"""Evaluation metrics for baseline literature summaries."""

from preprocess import tokenize


def word_count(text: str) -> int:
    """Count words in a string."""
    return len(tokenize(text))


def keyword_coverage(keywords: str) -> int:
    """Count extracted keywords."""
    if not isinstance(keywords, str) or not keywords.strip():
        return 0
    return len([k for k in keywords.split(";") if k.strip()])


def readability_proxy(text: str) -> float:
    """Simple readability proxy based on average words per sentence."""
    if not isinstance(text, str) or not text.strip():
        return 0.0
    sentences = [s for s in text.split(".") if s.strip()]
    if not sentences:
        return float(word_count(text))
    return round(word_count(text) / len(sentences), 2)
