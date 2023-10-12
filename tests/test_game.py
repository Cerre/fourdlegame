import pytest
from fourdle.fourdle import Fourdle  # Assuming you've named your module "fourdle.py"

def test_reset():
    game = Fourdle(["WANT", "BOLT", "FROG"])
    state = game.reset()
    assert state == ['W', 'W', 'W', 'W']

def test_validate_word():
    game = Fourdle(["WANT"])
    game.target_word = "WANT"
    hint = game.validate_word("WAND")
    assert hint == "GGGW"

def test_max_guesses():
    game = Fourdle(["WANT"])
    game.reset()
    for _ in range(game.max_guesses):
        _, _, done = game.step("BOLT")
    assert done == True

def test_correct_guess():
    game = Fourdle(["WANT"])
    game.reset()
    _, _, done = game.step("WANT")
    assert done == True

def test_get_reward():
    game = Fourdle(["WANT"])
    game.target_word = "WANT"
    reward = game._get_reward(['G', 'G', 'G', 'G'])
    assert reward == 1000

    reward = game._get_reward(['G', 'Y', 'Y', 'Y'])
    assert reward == 50

    reward = game._get_reward(['Y', 'Y', 'Y', 'Y'])
    assert reward == 25

    reward = game._get_reward(['W', 'W', 'W', 'W'])
    assert reward == -10

def test_render(capsys):  # capsys is a pytest built-in fixture to capture print statements
    game = Fourdle(["WANT"])
    game.reset()
    game.step("BOLT")
    game.render()
    captured = capsys.readouterr()  # Captures the print output
    assert "Current Hint:" in captured.out
    assert "Guesses left:" in captured.out

