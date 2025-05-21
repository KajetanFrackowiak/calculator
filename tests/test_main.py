# tests/test_main.py
import unittest.mock
import pytest
import main


@pytest.fixture(autouse=True)
def mock_hazelcast():
    """Mock both the hazelcast initialization and cache to prevent real connections"""
    # Mock the init_hazelcast function to do nothing
    with unittest.mock.patch.object(main, 'init_hazelcast'), \
            unittest.mock.patch.object(main, 'cache') as mock_cache:
        # Configure the mock cache behavior
        mock_cache.contains_key.return_value = False
        mock_cache.get.return_value = None
        mock_cache.put.return_value = None

        # Make sure cache is not None to prevent initialization attempts
        main.cache = mock_cache

        yield mock_cache


def test_add_with_cache(mock_hazelcast):
    # Test cache miss
    mock_hazelcast.contains_key.return_value = False

    result = main.cached_operation("add", 1, 2)

    assert result == 3
    mock_hazelcast.contains_key.assert_called_with("add:1:2")
    mock_hazelcast.put.assert_called_with("add:1:2", 3)


def test_add_with_cache_hit(mock_hazelcast):
    # Test cache hit
    mock_hazelcast.contains_key.return_value = True
    mock_hazelcast.get.return_value = 3

    result = main.cached_operation("add", 1, 2)

    assert result == 3
    mock_hazelcast.contains_key.assert_called_with("add:1:2")
    mock_hazelcast.get.assert_called_with("add:1:2")
    mock_hazelcast.put.assert_not_called()


def test_subtract_with_cache(mock_hazelcast):
    mock_hazelcast.contains_key.return_value = False

    result = main.cached_operation("subtract", 5, 3)

    assert result == 2
    mock_hazelcast.put.assert_called_with("subtract:5:3", 2)


def test_multiply_with_cache(mock_hazelcast):
    mock_hazelcast.contains_key.return_value = False

    result = main.cached_operation("multiply", 5, 3)

    assert result == 15
    mock_hazelcast.put.assert_called_with("multiply:5:3", 15)