# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game purpose:** A number guessing game built with Streamlit. The player guesses a secret number within a range set by the difficulty (Easy 1-20, Normal 1-100, Hard 1-50) and gets a higher/lower hint after each guess, until they win or run out of attempts.
- [x] **Bugs I found:**
  1. The hints were wrong. A guess of 50 against a secret of 22 said "Go HIGHER!". The hint messages in `check_guess` were swapped, and on even attempts the secret was converted to a string, so numbers were compared as text.
  2. Guesses outside the range (like 500 or -3) were accepted and still got a hint, because `parse_guess` never checked the range.
  3. The attempts counter was off by one, because it started at 1 instead of 0.
- [x] **Fixes I applied:**
  1. Moved `check_guess` into `logic_utils.py`, swapped the hint messages, and removed the string conversion of the secret in `app.py`.
  2. Moved `parse_guess` into `logic_utils.py` and added a range check that uses the current difficulty's low and high. `app.py` now imports both functions.
  3. I did not fix the attempts counter bug. It is documented in `reflection.md`.
- [x] **Tests:** I added pytest cases for the hint direction, number-vs-text comparison, and out-of-range guesses.

## 📸 Demo Walkthrough

1. I start a new game on Normal difficulty (range 1 to 100).
2. I enter 500. The game shows an error that the guess must be between 1 and 100, and gives no hint.
3. The secret is 22 and I enter 50. The game says "Go LOWER!".
4. I enter 10. The game says "Go HIGHER!".
5. I keep narrowing down until I enter 22. The game shows "Correct!", the balloons appear, and the game ends.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# python -m pytest
# ========================= 10 passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]