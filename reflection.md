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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.