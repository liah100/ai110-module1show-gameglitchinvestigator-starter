# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, it looked like a normal number guessing game with a text box, a submit button, and a sidebar for difficulty. Once I started playing, though, the behavior didn't match the rules. The hints sent me in the wrong direction, the attempts counter was off by one, and the game accepted guesses outside the 1-100 range and still gave hints for them.

1. **Wrong hints:** The secret was 22 and I guessed 50, but the game said "Go HIGHER!". The messages in `check_guess()` are swapped, and on even attempts the secret is converted to a string, so numbers get compared as text.
2. **Attempts counter off by one:** The counter starts at 1 before any guess is made, so it's counting a guess I haven't taken. The "New Game" button resets it to 0, so the game disagrees with itself.
3. **Out-of-range guesses get hints:** Numbers like 500 or -3 are accepted and still get a higher/lower hint. `parse_guess()` only checks that the input is a number, not that it's in range.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|-------|-------------------|-----------------|------------------------|-------------------------|
| Guess of 50 when the secret is 22 | "Go LOWER!" | "Go HIGHER!" | none | `app.py`, `check_guess()` (swapped messages) and the string conversion of `secret` in the `if submit:` block |
| New game, first guess on Normal | Counter starts at 0 and the first guess counts as attempt 1 | Counter starts at 1, so the count is off by one | none | `app.py`, `st.session_state.attempts = 1` |
| Guess of 500 (or -3) | Error saying the guess is out of range, no hint | Accepted, and the game says to go higher or lower | none | `app.py`, `parse_guess()` |

---

## 2. How did you use AI as a teammate?

- **Tools used:** I used an AI coding assistant in VS Code and Claude in chat to explain the bugs and help write the fixes and tests.
- **Correct suggestion:** I asked the AI to explain why a guess of 50 against a secret of 22 told me to go higher. It traced the logic step by step and found that the "Too High" and "Too Low" messages were swapped in `check_guess`. It also noticed that on even attempts the secret was converted to a string, so numbers were compared as text. I verified this by reading `check_guess` myself, then fixing it and replaying the same guess in the live game, which now said "Go LOWER!".
- **Suggestion I changed:** The AI's proposed fix only swapped the two messages and did not say to remove the string conversion. That would have left hints wrong on alternating guesses, because as text "9" is greater than "10". I removed the conversion as well and added a pytest (`check_guess(9, 10)` must return "Too Low") to prove numbers now compare as numbers.

---

## 3. Debugging and testing your fixes

- **How I decided a bug was fixed:** I replayed the exact input that triggered it in the live game (50 vs. a secret of 22 for the hints, and 500 or -3 for the range) and confirmed the behavior was right, then confirmed a pytest covering it passed.
- **Tests I ran:** I ran `python -m pytest`. At first the starter tests failed because `check_guess` returns a pair like `("Win", "🎉 Correct!")` and they expected only `"Win"`. I updated them to unpack the pair. I then added tests for swapped hints, text-vs-number comparison, and out-of-range guesses (500, -3, and 50 on Easy). All 10 pass.
- **How AI helped with tests:** The AI suggested which cases to test, including the "9" vs "10" case that targets the string-comparison bug. It also warned that the starter tests might fail, which saved me time diagnosing the first failures.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.