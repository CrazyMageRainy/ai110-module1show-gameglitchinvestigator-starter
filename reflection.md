# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  The hints are indeed higher (says go higher when it needs to go lower and visce versa).
  THe new game button appears to not function after you win. Does work while you haven't used all your attempts.
  Appear to allow attempts more than 8. It goes up more attempts (in history) or down more than it should. Also noticed something odd when continously submitting guesses at a certain intervals.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Using Gemnini via its vscode plugin. THe first bug with the secrets getting swapped was correctly found with claude. IT was caused
by an if statement where the results were swapped. The suggestion theAI gave me for this wasn't wrong, but it wasn't the best approach as the fix would have been easier bu changing the '>' to a '<', insteading of swapping the resulting code.
WHen I ask about the logic of the app's game states. It tells me about new bugs with it. The new game bug I saw before was also mentioned.
It also says there is a bug in attempts in which the attempts is incorrectly reseting to 0 when the initial setup had it at 1, which changes the num of attempts after a reset. It also claims that the secret ignores the difficulty, choosing a number not within the intented range for said difficulty.
Also another bug I also noticed but wasn't unsure of os that history and scores carry over.
For the state Logic, it recommended me a seperate function to seperate it from the main code ``reset_game()``. It resets the attempts, secret, as well as the status of the st (whats holding the apps state). This fixes our main issue with game not resetting but also the issue of not respecting the difficulty's range.
The ai confirms and identifies where I tagged for attempts, where on even guesses it gets converted into a string and not an intger, which would cause logic errors from the TypeErrors when comparing to the secret number

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

For the First bug claude show that it corrected the logic error from the if statment for the hints. It helped me designed the tests for it, since the tests
that are already inside it appear to have some issues of its own. They were outputing AssertionError from the statements, since the statements weren't just "Win",
it was also had emoji and is a full statements.
 Claude created this function to seperate the restart game. It changes the values into defaults as well as change the states back to "playing",
 fixing the issue of the game not restarting after a win or lose. The value of secret number correctly follows the difficulties range.
 It wasnt able to give a useful pytest for when the even attempts where being converted into ints, mainly cause where the bug was wasn't in its own function.
 Another fix was with the game accepting an empty input, for example, as a incorrect attempt. Claude showed that removing it from appending to our history array and nmoving the line to add attempts value by one when its correct solved this issue. It gave a test for it by testing whether an input can be a None value, an empty string, aphabets and the integers. This should be the expected inputs the app might recieved from the user. 
 
 Claude has a much easier time making tests for code if the code is inside a function, while for bugs that are in t he main file code and not in a function is more difficult to make since you can't input custom variables to test the scenario (example: the even number of attempts causing the input to be turned into an integer). Modularity is more friendly for the  AI, and it also is likely to create new functions, like the ``reset_game`` function to sepereate the reseting from the rest of the code.
 The bugs are considered fixed for me when the logic for them appear to be respected while playing the games. I expect it to make a new clean game whenver i press the state or when the random number is within the range it was given for the difficulty. THe AI does help look at the logic of the code, and gives a decent explanation for it. It works well with smaller bugs, but sometimes it does do extra to fix some which could be fixed in a much simplier way like when comparing the secret and attempt to give a clue.

 Therefore, tests in general are much easier to do for individual functions than for code thats written in the main function. And simplier tests are much easier to create and maintaing using AI.
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
