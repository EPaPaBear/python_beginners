# Python Loops: Week 3 Cheat Sheet

**The `while` Loop (Repeat until told to stop)**
* Runs code over and over as long as a condition is `True`.
* **WARNING:** If you forget to change the condition inside the loop, it will run forever (an Infinite Loop). Press `Ctrl + C` in the terminal to kill it!

**The `for` Loop (Iterate through a collection)**
* Strings are just collections of characters. You can loop through a string letter by letter.
* Example:
`for letter in "Secret":`
`print(letter)`


**Building Strings (The Accumulator)**
* You can add letters together to build new words using `+=`.
* `word = "Bat"`
* `word += "man"` *(word is now "Batman")*


**ASCII Magic (Letters are Numbers)**
Computers don't know letters, they only know numbers. Every letter has a secret numerical code.
* `ord("a")` -> Turns a letter into its number (97).
* `chr(97)` -> Turns a number back into a letter ("a").