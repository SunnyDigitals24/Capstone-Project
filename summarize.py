"""Baseline summarization functions.

This module intentionally uses a simple baseline method. Later versions of the
project can compare this output with LLM-generated summaries.
"""

from preprocess import clean_text


def baseline_summary(text: str, max_sentences: int = 2) -> str:
    """Create a simple summary by returning the first few sentences."""
    text = clean_text(text)
    if not text:
        return ""

    sentences = [s.strip() for s in text.split(".") if s.strip()]
    selected = sentences[:max_sentences]

    if not selected:
        return text

    return ". ".join(selected) + "."


def extract_keywords(text: str) -> str:
    """Extract mental-health and AI-related keywords from text."""
    keyword_list = [
        "depression", "depressive", "anxiety", "stress", "sleep",
        "well-being", "mental health", "students", "college", "university",
        "social media", "literature review", "artificial intelligence",
        "large language models", "summarization", "screening", "support"
    ]

    text_lower = text.lower()
    found = []

    for keyword in keyword_list:
        if keyword in text_lower:
            found.append(keyword)

    return "; ".join(sorted(set(found)))
