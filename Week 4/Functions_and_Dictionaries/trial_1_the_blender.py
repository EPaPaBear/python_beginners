# ==========================================
# TRIAL 1: THE BLENDER
# ==========================================
# We need to build a function that calculates a damage multiplier for a video game.

# TODO: Build the function.
# 1. Define a function called 'calculate_damage' that takes two arguments: 'base_damage' and 'multiplier'.
# 2. Inside the function, multiply them together.
# 3. RETURN the final result.

# --- Write your function below ---



# --- Do not change the code below ---
print("Testing the function...")
strike_one = calculate_damage(10, 2)
strike_two = calculate_damage(5, 5)

print(f"Strike One dealt {strike_one} damage.")
print(f"Strike Two dealt {strike_two} damage.")
print(f"Total Damage: {strike_one + strike_two}")