# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  The hints are indeed higher (says go higher when it needs to go lower and visce versa).
  THe new game button appears to not function after you win. Does work while you haven't used all your attempts.
  Appear to allow attempts more than 8. It goes up more attempts (in history)

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Using Gemnini via its vscode plugin. THe first bug with the secrets getting swapped was correctly found with claude. IT was caused
by an if statement where the results were swapped.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
For the First bug claude show that it corrected the logic error from the if statment for the hints. It helped me designed the tests for it, since the tests
that are already inside it appear to have some issues of its own. They were outputing AssertionError from the statements, since the statements weren't just "Win",
it was also had emoji and is a full statements.
---

## 4. What did you learn about Streamlit and state?
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit uses states for the game. There are the "playing" , "won", and "lost" state. WHen the game is running, it will be in the playing state. It changes the other
states depending whether you win or lost the game. What it should do when you rerun the game via the new game button is return the game to a "clean slate" and change the 
state back to "playing". The states contain the variables used to keep track of the game itself, such as the secret number and the number of tries per the game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
