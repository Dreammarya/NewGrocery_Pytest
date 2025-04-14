import pytest
from count_word_matches import count_word_matches

@pytest.mark.parametrize("text, target, expected", [
    ("", "word", 0),  # Пустой текст
    ("hello world", "", 0),  # Пустая цель
    ("", "", 0),  # Оба пустые
    ("hello  world", "world", 1),  # Лишние пробелы
    (" cat ", "cat", 1),  # Leading/Trailing Spaces
    ("cat,dog cat", "cat", 1),  # Punctuation Not Handled
    ("x y z", "x", 1)  # Однобуквенные слова
])
def test_count_word_matches(text, target, expected):
    actual = count_word_matches(text, target)
    assert actual == expected, f"Error: expected {expected}, but result is {actual}"
