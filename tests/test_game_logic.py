from logic_utils import check_guess, parse_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_says_go_lower():
    # Guess 50 vs secret 22: guess is too high, so the hint should say LOWER
    outcome, message = check_guess(50, 22)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_says_go_higher():
    outcome, message = check_guess(10, 22)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_numbers_compare_as_numbers_not_text():
    # As text, "9" > "10" is True. As numbers, 9 is too low.
    outcome, message = check_guess(9, 10)
    assert outcome == "Too Low"

def test_out_of_range_high_rejected():
    ok, value, err = parse_guess("500", 1, 100)
    assert ok is False
    assert value is None


def test_out_of_range_low_rejected():
    ok, value, err = parse_guess("-3", 1, 100)
    assert ok is False


def test_in_range_accepted():
    ok, value, err = parse_guess("50", 1, 100)
    assert ok is True
    assert value == 50


def test_range_respects_difficulty():
    # 50 is fine on Normal but out of range on Easy (1-20)
    ok, value, err = parse_guess("50", 1, 20)
    assert ok is False