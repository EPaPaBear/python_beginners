import tkinter as tk

def decode_decimal():
    try:
        num = int(entry_input.get()) # Read as normal Base 10
        char = chr(num)
        label_result.config(text=f"Character: {char}")
    except ValueError:
        label_result.config(text="Error: Invalid Decimal!")

def decode_binary():
    try:
        # The '2' tells Python to read the string as Base 2
        num = int(entry_input.get(), 2) 
        char = chr(num)
        label_result.config(text=f"Character: {char}")
    except ValueError:
        label_result.config(text="Error: Invalid Binary!")

# --- GUI Setup ---
window = tk.Tk()
window.title("Signal Injector")
window.geometry("300x250")

tk.Label(window, text="Enter a Decimal or Binary number:").pack(pady=10)

entry_input = tk.Entry(window, font=("Courier", 14), justify="center")
entry_input.pack()

# Decimal Button
tk.Button(window, text="Decode Base 10 (Decimal)", command=decode_decimal).pack(pady=5)

# Binary Button
tk.Button(window, text="Decode Base 2 (Binary)", command=decode_binary).pack(pady=5)

label_result = tk.Label(window, text="Character: -", font=("Courier", 16, "bold"), fg="green")
label_result.pack(pady=20)

window.mainloop()