import pytest
from count_word_matches import count_word_matches

@pytest.mark.parametrize("text, target, expected", [
    ("", "word", 0),  # empty text
    ("hello world", "", 0),  # emptytarget
    ("", "", 0),  # bothempty
    ("hello  world", "world", 1),  # extraspaces
    (" cat ", "cat", 1),  # Leading/Trailing Spaces
    ("cat,dog cat", "cat", 1),  # Punctuation Not Handled
    ("x y z", "x", 1)  # 1letterwords
])
def test_count_word_matches(text, target, expected):
    actual = count_word_matches(text, target)
    assert actual == expected, f"Error: expected {expected}, but result is {actual}"
