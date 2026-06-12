# Python Organization: Week 4 Cheat Sheet


**Functions (The `def` Keyword)**
A function is a reusable block of code. It doesn't run until you "call" it.
* **Defining it:** `def say_hello(name):`
* **Calling it:** `say_hello("Alex")`


**The `return` Statement (The Black Box)**
`print()` just shows data to the human. `return` actually gives data back to the computer so you can use it in math or variables later.
* `def add(a, b):`
* `    return a + b`
* `total = add(5, 10)` *(total is now 15)*


**Dictionaries (The `{}` Brackets)**
A dictionary stores data in **Key : Value** pairs. It is like a real dictionary: you look up a word (the Key) to find the definition (the Value).
* **Creating:** `passwords = {"admin": "1234", "guest": "0000"}`
* **Looking up:** `print(passwords["admin"])` *(Prints "1234")*
* **Adding new data:** `passwords["user1"] = "qwerty"`