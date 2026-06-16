from pathlib import Path
import duckdb


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"


def ensure_directory(path: Path) -> None:
    """Create a directory if it does not exist."""
    path.mkdir(parents=True, exist_ok=True)


def file_exists(path: Path) -> bool:
    """Check whether a file exists."""
    return path.exists() and path.is_file()


def get_duckdb_connection(database_path: str = ":memory:") -> duckdb.DuckDBPyConnection:
    """Create a DuckDB connection."""
    return duckdb.connect(database_path)