from types import SimpleNamespace
from logic_utils import check_guess, reset_game

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    (result, message) = check_guess(50, 50)
    assert result == "Win"

# def test_guess_too_high():
#     # If secret is 50 and guess is 60, hint should be "Too High"
#     result = check_guess(60, 50)
#     assert result == "Too High"

# def test_guess_too_low():
#     # If secret is 50 and guess is 40, hint should be "Too Low"
#     result = check_guess(40, 50)
#     assert result == "Too Low"

def test_hint_too_high_says_go_lower():
    # Bug fix: when guess is too high, hint should say Go LOWER, not Go HIGHER
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message

def test_reset_game_restores_playing_status():
    # Bug fix: after a won/lost game, reset_game should set status back to "playing"
    state = SimpleNamespace(attempts=8, secret=42, status="won")
    reset_game(state, 1, 100)
    assert state.status == "playing"
    assert state.attempts == 0

def test_hint_too_low_says_go_higher():
    # Bug fix: when guess is too low, hint should say Go HIGHER, not Go LOWER
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message
