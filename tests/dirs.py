from pathlib import Path

test_root = Path(__file__).parent

def get_test_data_dir():
    return test_root / "test_data"