def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

# modified its header to grab the low and high range of the difficulty, and sending an error message telling user that their guess is beyond the range
def parse_guess(raw: str, low: int = None, high: int = None):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if low is not None and high is not None:
        if not (low <= value <= high):
            return False, None, f"Please enter a number between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        #claude figured out that this if statement is the culprit to the clues being reversed. It suggested swapping the
        # statments of the if statement instead of changing the > sign to the < sign.
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

# Claude created this function to seperate the restart game. It changes the values into defaults as well as change the states back to "playing"
# fixing the issue of the game not restarting after a win or lose. The value of secret number correctly follows the difficulties range
def reset_game(state, low: int, high: int):
    """Reset session state for a new game."""
    import random
    state.attempts = 0
    state.secret = random.randint(low, high)
    state.status = "playing"

# Cluade moved the function here. It fixes the bug where it fixes the score from changing when attempt number is even
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
