# ==========================================
# EXERCISE 3: THE ENGINEER (PROBLEM SOLVING)
# ==========================================
# The Problem: The vault is locked by a security system. 
# You need to write a "Number Guesser" program to crack it.
#
# YOUR MISSION:
# Build the program from scratch using the toolbox you've learned.
# 
# THE SPECIFICATIONS (Read carefully!):
# 1. The computer has a secret password (an integer between 1 and 100).
#    (I have provided the random number generator for you).
# 2. You have a 'while' loop that asks the user to guess the password.
# 3. If they guess too high, print "Access Denied. Too high."
# 4. If they guess too low, print "Access Denied. Too low."
# 5. If they guess exactly right, print "ACCESS GRANTED", and break the loop.

import random

# The secret password is generated here:
secret_password = random.randint(1, 100)
print("SYSTEM LOCKED. Enter numeric passcode.")

# TODO: Build the system below! 
# Hint: You will need a 'while True' loop, input(), int(), and if/elif/else.