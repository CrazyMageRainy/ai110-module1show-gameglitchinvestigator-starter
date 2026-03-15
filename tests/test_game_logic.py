from types import SimpleNamespace
from logic_utils import check_guess, reset_game, parse_guess

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

#tests whether its correctly dealing with incompatible inputs
def test_empty_guess_is_invalid():
    # Bug fix: empty input should fail validation, not count as an attempt
    ok, guess_int, err = parse_guess("")
    assert ok == False
    assert guess_int is None
    assert err is not None

def test_none_guess_is_invalid():
    # Bug fix: None input should fail validation, not count as an attempt
    ok, guess_int, err = parse_guess(None)
    assert ok == False
    assert guess_int is None
    assert err is not None

def test_non_number_guess_is_invalid():
    # Non-numeric input should also fail validation without counting as an attempt
    ok, guess_int, err = parse_guess("abc")
    assert ok == False
    assert guess_int is None
    assert err is not None

def test_valid_guess_is_accepted():
    # A valid numeric string should parse successfully
    ok, guess_int, err = parse_guess("42")
    assert ok == True
    assert guess_int == 42
    assert err is None
