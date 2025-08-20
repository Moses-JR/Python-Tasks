import tkinter as tk

# Function to update the display
def button_click(symbol):
    current = display.get()
    if current == "Error":
        display.set("")
    display.set(current + symbol)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(display.get())
        display.set(result)
    except Exception as e:
        display.set("Error")

# Function to clear the display
def clear():
    display.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# StringVar to track the display
display = tk.StringVar()
display.set("")

# Entry widget to display the expression
entry = tk.Entry(root, textvariable=display, justify="right", font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), command=lambda symbol=text: button_click(symbol))
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

# Clear button
clear_button = tk.Button(root, text="C", font=("Arial", 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Exit button
exit_button = tk.Button(root, text="Exit", font=("Arial", 18), command=root.quit)
exit_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# Configure grid rows and columns to expand with window resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
