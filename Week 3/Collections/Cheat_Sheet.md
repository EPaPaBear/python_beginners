# Python Collections: Week 3.5 Cheat Sheet


**The List (The `[]` Brackets)**
A list is a single variable that holds multiple pieces of data in a specific order.
* `inventory = ["Sword", "Shield", "Potion"]`


**Indices (Finding your stuff)**
Computers start counting at `0`.
* `print(inventory[0])` ➡️ Prints "Sword"
* `print(inventory[1])` ➡️ Prints "Shield"


**List Methods (Changing your stuff)**
* `inventory.append("Map")` : Adds "Map" to the end of the list.
* `inventory.pop()` : Removes and returns the very last item.
* `inventory.remove("Shield")` : Searches for "Shield" and deletes it.
* `len(inventory)` : Tells you how many items are in the list.


**Looping a List**
The exact same `for` loop from last week works on lists!
* `for item in inventory:`
* `    print(item)`