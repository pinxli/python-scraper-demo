from scraper import get_files


def test_get_files_returns_list():
    result = get_files("https://example.com")
    assert isinstance(result, list)