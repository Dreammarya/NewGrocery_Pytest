import pytest
from count_word_matches import count_word_matches

@pytest.mark.parametrize("text, target", [
    (None, "word"),  # None в качестве текста
    ("hello world", None),  # None в качестве цели
    (123, "word"),  # Число в качестве текста
    ("hello world", 456),  # Число в качестве цели
    (["hello", "world"], "world"),  # Список вместо строки (текст)
    ("hello world", ["world"])  # Список вместо строки (цель)
])
def test_invalid_inputs(text, target):
    with pytest.raises(TypeError):
        count_word_matches(text, target)