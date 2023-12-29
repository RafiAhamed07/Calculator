import tkinter as tk

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def backspace():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except (SyntaxError, ZeroDivisionError, ValueError) as e:
        clear_field()
        error_message = f"Error: {str(e)}"
        text_result.insert(1.0, error_message)


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.title("Beautiful Calculator")
root.iconbitmap(r'calculator.ico')

# Configure colors and fonts
bg_color = "#f0f0f0"
button_bg_color = "#d9d9d9"
button_fg_color = "black"
equal_button_color = "#66bb6a"  # Green color for equal button
font_style = ("Arial", 14)

# Set background color
root.configure(bg=bg_color)

# Configure text result box
text_result = tk.Text(root, height=2, width=16, font=font_style)
text_result.grid(columnspan=6, pady=10, padx=10, sticky="nsew")
text_result.configure(bg=bg_color)

# Button configuration
button_config = {
    "width": 5,
    "font": font_style,
    "bg": button_bg_color,
    "fg": button_fg_color,
    "bd": 2,
}

# Create buttons
buttons = [
    ('1', 2, 1), ('2', 2, 2), ('3', 2, 3),
    ('4', 3, 1), ('5', 3, 2), ('6', 3, 3),
    ('7', 4, 1), ('8', 4, 2), ('9', 4, 3),
    ('0', 5, 2), ('+', 2, 4), ('-', 3, 4),
    ('*', 4, 4), ('/', 5, 4), ('(', 5, 1),
    (')', 5, 3), ('←', 5, 2),
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, command=lambda t=text: button_click(t), **button_config)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Equal button
btnEqual = tk.Button(root, text='=', command=evaluate_calculation, width=11, font=font_style, bg=equal_button_color,
                     fg="white")
btnEqual.grid(row=6, column=1, columnspan=2, pady=10, padx=10, sticky="nsew")

# Clear button
btnClear = tk.Button(root, text="C", command=clear_field, width=11, font=font_style, bg="#ff704d", fg="white")
btnClear.grid(row=6, column=3, columnspan=2, pady=10, padx=10, sticky="nsew")

# Configure grid weights for responsiveness
for i in range(1, 7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


def button_click(symbol):
    if symbol == '←':
        backspace()
    else:
        add_to_calculation(symbol)


root.mainloop()
