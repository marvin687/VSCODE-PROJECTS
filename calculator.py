import tkinter
import math


button_values =[

["AC", "+/-", "%", "/"],
["7", "8", "9", "*"],
["4", "5", "6", "-"],
["1", "2", "3", "+"],
["0", ".", "√", "="]

]

row_count = len(button_values) #5
column_count = len(button_values[0])
right_symbols = [ "/", "*", "-", "+", "="  ]
top_symbols = [ "AC", "+/-", "%" ]

Background_darkgrey = "#1e1e1e" 
Buttons = "#333333"
Text = "#ffffff"
colors = {
    "/": "#ff9500",
    "*": "#ff9500",
    "-": "#ff9500",
    "+": "#ff9500",
    "=": "#34c759"
}
# window setup
window = tkinter.Tk() #create the window
window.title("Calculator")
window.resizable(False,False)
frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = "0", font =("arial", 45), 
                       bg="#000000", fg="#FFFFFF", anchor="e")

label.grid(row=0,column=0, columnspan = column_count, sticky ="we")
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]

        button = tkinter.Button(
            frame,
            text=value,
            font=("Arial", 30),
            width=column_count - 1,
            height=1,
            command=lambda value=value: button_clicked(value)
        )

        if value in top_symbols:
            button.config(fg="#000000", bg="#F0F0F0")

        elif value in right_symbols:
            button.config(fg="#FFFFFF", bg="#FF8C00")
        else:
            button.config(fg="#000000", bg="#D3D3D3")
        button.grid(row=row +1, column=column)

frame.pack()

# --- Logic Variables ---
current_expression = ""
result_shown = False


def button_clicked(value):
    global current_expression, result_shown
    
    # 1. Clear everything
    if value == "AC":
        current_expression = ""
        label.config(text="0")
    
    # 2. Perform the calculation
    elif value == "=":
        try:
            # eval() calculates the string (e.g., "7*8+2")
            result = str(eval(current_expression))
            label.config(text=result)
            current_expression = result
            result_shown = True
        except ZeroDivisionError:
            label.config(text="Error")
            current_expression = ""
        except:
            label.config(text="Error")
            current_expression = ""

    # 3. Square Root logic
    elif value == "√":
        try:
            # We convert current text to float, get root, then back to string
            res = math.sqrt(float(current_expression))
            # Formatting to remove .0 if it's a whole number
            res_str = f"{res:g}" 
            label.config(text=res_str)
            current_expression = res_str
            result_shown = True
        except:
            label.config(text="Error")
            current_expression = ""

    # 4. Toggle Positive/Negative
    elif value == "+/-":
        if current_expression:
            if current_expression.startswith("-"):
                current_expression = current_expression[1:]
            else:
                current_expression = "-" + current_expression
            label.config(text=current_expression)

    # 5. Percentage
    elif value == "%":
        try:
            res = float(current_expression) / 100
            current_expression = str(res)
            label.config(text=current_expression)
        except:
            pass

    # 6. Standard numbers and operators
    else:
        # If a result was just shown and you press a number, clear and start new
        if result_shown and value.isdigit():
            current_expression = value
        else:
            current_expression += str(value)
        
        result_shown = False
        label.config(text=current_expression)
# center the window
window.update()  # update window with the new size dimensions

window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()