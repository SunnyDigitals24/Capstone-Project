import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from preprocess import clean_text, tokenize
from summarize import baseline_summary, extract_keywords
from evaluate import word_count, keyword_coverage


def test_clean_text_removes_extra_spaces():
    assert clean_text("hello    world") == "hello world"


def test_tokenize_returns_words():
    assert tokenize("Sleep and anxiety.") == ["sleep", "and", "anxiety"]


def test_baseline_summary_returns_text():
    text = "This is sentence one. This is sentence two. This is sentence three."
    result = baseline_summary(text, max_sentences=2)
    assert "sentence one" in result.lower()
    assert "sentence two" in result.lower()


def test_extract_keywords_finds_terms():
    text = "This study discusses depression, anxiety, and sleep among students."
    keywords = extract_keywords(text)
    assert "depression" in keywords
    assert "anxiety" in keywords
    assert "sleep" in keywords


def test_word_count():
    assert word_count("mental health research") == 3


def test_keyword_coverage():
    assert keyword_coverage("depression; anxiety; sleep") == 3
