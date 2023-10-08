import pytest
from fourdle.fourdle import Fourdle
@pytest.mark.parametrize(
    "target_word,guess,expected_hint",
    [
        ("WANT", "AAAA", "WGWW"),
        ("WANT", "ANAS", "YYWW"),
        ("WANT", "WANT", "GGGG"),
        ("WANT", "WANA", "GGGW"),
        ("WANT", "NWAT", "YYYG"),
        ("WANT", "WXYZ", "GWWW")
    ]
)
def test_validate_word(target_word, guess, expected_hint):
    game = Fourdle([])
    game.set_target_word(target_word)
    hint = game.validate_word(guess)
    assert hint == expected_hint

# Optional: Additional test for the case where both target_word and guess have repeating letters
@pytest.mark.parametrize(
    "target_word,guess,expected_hint",
    [
        ("BOOK", "BOBO", "GGWY"),
    ]
)
def test_validate_word_with_repeating_letters(target_word, guess, expected_hint):
    game = Fourdle([])
    game.set_target_word(target_word)
    hint = game.validate_word(guess)
    assert hint == expected_hint
