import tkinter as tk

#Function to update the display with button click
def btn_click(val):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + val)

# Fuction to calculate
def cal():
    try:
        res = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(res))

    except:
        display.delete(0, tk.END)
        display.insert(0, "ERROR")

# Function to clear
def clear_display():
    display.delete(0, tk.END)

#Create the main window 창만글기
window = tk.Tk()
window.title("Calculator")

# display Area
display = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4)


# button layout
btn = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('-', 4, 2), ('=', 4, 3)
]

# Create button and place them in the window

for (text, row, col) in btn:
    if text == "=":
        tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=cal).grid(row=row, column=col)
    elif text == "C":
        tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=clear_display).grid(row=row, column=col)        
    else:
        tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=lambda val=text: btn_click(val)).grid(row=row, column=col)


#start application
window.mainloop()