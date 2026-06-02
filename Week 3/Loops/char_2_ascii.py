import tkinter as tk

def intercept_signal():
    char = entry_input.get()
    
    # We only want to process one character at a time
    if len(char) != 1:
        label_decimal.config(text="Error: Enter exactly ONE character.")
        label_binary.config(text="")
        return
        
    # The Core Logic
    base_10 = ord(char)
    base_2 = bin(base_10) # Turns 97 into '0b1100001'
    
    # Update the UI
    label_decimal.config(text=f"Base 10 (Decimal): {base_10}")
    label_binary.config(text=f"Base 2 (Binary): {base_2}")

# --- GUI Setup ---
window = tk.Tk()
window.title("Signal Interceptor")
window.geometry("300x200")

tk.Label(window, text="Enter a single character:").pack(pady=10)

entry_input = tk.Entry(window, font=("Courier", 14), justify="center")
entry_input.pack()

tk.Button(window, text="Intercept", command=intercept_signal).pack(pady=10)

label_decimal = tk.Label(window, text="Base 10 (Decimal): -", font=("Courier", 12))
label_decimal.pack()

label_binary = tk.Label(window, text="Base 2 (Binary): -", font=("Courier", 12))
label_binary.pack()

window.mainloop()