# tests/test_main.py
from main import cached_operation
from unittest.mock import MagicMock

def test_add_with_cache():
    mock_cache = MagicMock()
    mock_cache.contains_key.return_value = False
    mock_cache.get.return_value = None
    mock_cache.put.return_value = None

    result = cached_operation("add", 1, 2)
    assert result == 3

def test_subtract_with_cache():
    mock_cache = MagicMock()
    mock_cache.contains_key.return_value = False
    mock_cache.get.return_value = None
    mock_cache.put.return_value = None

    result = cached_operation("subtract", 5, 3)
    assert result == 2

def test_multiply_with_cache():
    mock_cache = MagicMock()
    mock_cache.contains_key.return_value = False
    mock_cache.get.return_value = None
    mock_cache.put.return_value = None

    result = cached_operation("multiply", 5, 3)
    assert result == 15
