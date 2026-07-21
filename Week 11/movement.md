---
marp: true
theme: default
class: invert
paginate: false
---


# 🎮 Taking Control
## Smooth Movement and Invisible Cages
### (Week 11: Player Input & Boundaries)

---

## ⌨️ Single Click vs. Holding Down
In games, there are two ways to use a keyboard:
1. Events (Single Click): Good for jumping, pausing, or shooting a single bullet. You don't want to accidentally shoot 60 bullets if you hold the key a fraction of a second too long.
2. Polling (Holding Down): Good for walking/moving. You want the computer to constantly check: "Is the key still being held down right now?"

---

🏃 Smooth Movement with `pygame.key.get_pressed()` To make our character walk smoothly, we poll the keyboard every single frame:
```python
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_LEFT]:
        player_x -= 5
``` 
Notice we use `if` statements, not `elif`.Why? Because if we used `elif`, we wouldn't be able to press Up and Right at the same time to move diagonally!

---

## 🧱 The Problem: We Escaped!
If you add movement code, your character can simply walk off the edge of the monitor into the abyss. The computer doesn't know the screen has an edge unless you tell it.
We need Boundary Detection.

---

## 🚧 Building the Invisible Cage
Before we draw the picture, we do a security check on the player's X and Y coordinates. If they went too far, we physically push them back inside.
```py
    # Did they walk off the left side?
    if player_x < 0:
        player_x = 0  # Push them back to the edge!
```

---

## 📏 The Right Side & Bottom
The left and top walls are easy: they are always `0`.But what about the right side? If our screen width is `800`, we can't just check if `player_x > 800`.

Because Pygame draws rectangles from the Top-Left Corner, the player will disappear before we push them back.We must subtract the player's width from the screen width!
```py
    if player_x > (800 - player_width):
```

---

## 🎯 The Mission
Today, we are wiring up the controller. Open your canvas. Add WASD or Arrow Key controls. 

Then, build an impenetrable fortress of if statements around your screen so your player can never escape.