# TESTS: this is a basic example of a test run by pytest.
# If your project doesn't have tests (yet!?) you don't need this file or the
# tests/ directory.

from pkgsample.add import add


def test_simple():
    assert add(17, 23) == 40
