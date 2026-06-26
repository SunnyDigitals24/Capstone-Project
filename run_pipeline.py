"""Run the baseline mental health literature review pipeline."""

from summarize import baseline_summary, extract_keywords
from evaluate import word_count, keyword_coverage, readability_proxy
from utils import load_dataset, save_results, dataset_overview


def main() -> None:
    df = load_dataset()

    df["clean_summary"] = df["abstract"].apply(baseline_summary)
    df["keywords_extracted"] = df["abstract"].apply(extract_keywords)
    df["abstract_word_count"] = df["abstract"].apply(word_count)
    df["summary_word_count"] = df["clean_summary"].apply(word_count)
    df["keyword_count"] = df["keywords_extracted"].apply(keyword_coverage)
    df["readability_proxy"] = df["clean_summary"].apply(readability_proxy)

    output_path = save_results(df)

    print("Pipeline completed successfully.")
    print(f"Dataset overview: {dataset_overview(df)}")
    print(f"Results saved to: {output_path}")


if __name__ == "__main__":
    main()
