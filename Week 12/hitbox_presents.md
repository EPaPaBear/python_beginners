---
marp: true
theme: default
class: invert
paginate: true
---

# The Logic of Touch
## Hitboxes & Collision Detection

(Week 11: Adding Game Mechanics)

---

# What is a Hitbox?

In video games, the computer doesn't care what your character looks like. It doesn't care if it's a Mario sprite or a highly detailed 3D dragon.

To calculate physics, the computer draws an invisible Bounding Box around your character. This is your Hitbox.

If an enemy laser touches the invisible box, you take damage, even if it didn't touch the actual drawing of your character!

---

# The Math (Too Hard!)

To check if two rectangles are touching, you have to compare their X and Y coordinates on all four sides:

```py
if (player_x < coin_x + coin_width and
    player_x + player_width > coin_x and
    player_y < coin_y + coin_height and
    player_y + player_height > coin_y):
    print("They touched!")
```

Yikes. That is way too much math to write every time we want to pick up an item.

---

# The Engine Shortcut: colliderect

Because checking for collisions is the most common thing in games, the Pygame Engine has a built-in sensor.

Instead of math, we just ask one rectangle if it is overlapping with another rectangle. It returns True or False.

```py
if player_rect.colliderect(coin_rect):
    print("Ding! You got a coin!")
```

---

# The Teleportation Trick

What happens when you collect a coin in a game? Does the coin actually get destroyed and deleted from the computer's memory?

Usually, no.

It is much faster for the computer to just teleport the existing coin to a random new (X, Y) coordinate on the screen. To the player, it looks like a brand-new coin spawned!

We use `random.randint(min, max)` to pick the new coordinates.

---

# The Mission

Today, we are building The Coin Collector.

You have a player and a coin. You will wire up the colliderect sensor. When they touch, you will increase a score variable, and instantly teleport the coin to a random X and Y location.