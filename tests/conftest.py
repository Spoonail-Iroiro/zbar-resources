import pytest
from tests.dirs import get_test_data_dir


@pytest.fixture
def test_data_dir():
    return get_test_data_dir()