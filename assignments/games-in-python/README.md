
# 🎮 Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game that quizzes players on hidden words, practicing string manipulation, control flow, and user input handling.

## 📝 Tasks

### 🛠️ Implement the Hangman game

#### Description
Create a Python program that:

- Randomly selects a secret word from a predefined list
- Repeatedly prompts the player to guess a single letter
- Reveals correct letter positions and displays remaining attempts
- Ends the game when the player guesses the word or runs out of attempts

#### Requirements
Completed program should:

- Use a list of words and select one at random
- Display the current progress (e.g., `_ a _ _ m a n`)
- Accept only single-letter guesses and ignore repeated guesses
- Track and show remaining incorrect attempts
- Print a clear win or lose message and reveal the secret word on loss

## ⏱ Estimated time

30–60 minutes

## ⚙️ Difficulty

Easy / Beginner

## 💡 Hints

- Use `random.choice()` to pick a word
- Store guessed letters in a set for quick lookups
- Build the display string by joining characters or `_` placeholders

## 📦 Starter code

See `starter-code.py` in this folder for a minimal starting point.

## ✅ Example session

```
Welcome to Hangman!
Word: _ _ _ _ _
Guess a letter: a
Correct! Word: _ a _ _ _
Guess a letter: n
Incorrect. Attempts left: 4
...
You win! The word was: "apple"
```

---

If you'd like, I can also add unit tests or expand the starter code with input validation.
