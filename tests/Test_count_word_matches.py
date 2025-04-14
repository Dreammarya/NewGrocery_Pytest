import pytest
from count_word_matches import count_word_matches

@pytest.mark.parametrize("text, target, expected", [
    ("The cat sat on the mat", "cat", 1),
    ("Dog dog DOG dOg", "dog", 4),
    ("Hello world", "world", 1),
    ("hello hello HELLO", "hello", 3),
    ("No matches here", "yes", 0),
    ("catcat cat catdog", "cat", 1),
    ("a a a", "a", 3),
])
def test_count_word_matches(text, target, expected):
    actual = count_word_matches(text, target)
    assert actual == expected, f"Error: expected {expected}, but result is {actual}"
