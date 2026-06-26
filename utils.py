"""General utility functions for the capstone project."""

from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"


def load_dataset(filename: str = "mental_health_literature.csv") -> pd.DataFrame:
    """Load a CSV dataset from the data folder."""
    path = DATA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path)


def save_results(df: pd.DataFrame, filename: str = "summary_results.csv") -> Path:
    """Save result dataframe to the outputs folder."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / filename
    df.to_csv(output_path, index=False)
    return output_path


def dataset_overview(df: pd.DataFrame) -> dict:
    """Return a small overview of the dataset."""
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "topics": sorted(df["topic"].dropna().unique().tolist()) if "topic" in df else []
    }
