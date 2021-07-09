# HELLO GUI

# ----------- window basic ------------

import tkinter
from tkinter.constants import BOTH, END
from tkinter import StringVar
from tkinter.font import names
from typing import Text

# -------------- window display --------------
root = tkinter.Tk()
root.title("Hello GUI app")
root.iconbitmap("wave.ico")
root.resizable(0, 0)
root.geometry("400x400")

# ----------------- define color and font ----------------
root_color = "#9FFFCB"
input_color = "#004E64"
output_color = "#7AE582"
root.config(bg=root_color)

# -------------- define functions -----------------


def submit_name():
    '''Say hello to the user'''
    # create a label for the user name based on radio button values
    if case_style.get() == 'normal':
        name_label = tkinter.Label(
            output_frame, text="Hello " + name.get(), bg=output_color)
    elif case_style.get() == 'upper':
        name_label = tkinter.Label(output_frame, text=(
            "Hello " + name.get()).upper(), bg=output_color)

    # pack label on the screen
    name_label.pack()

    # clear the entry field for the next user
    name.delete(0, END)


# -------------- define layout ----------------
# define frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0, 10), fill=BOTH, expand=True)

# ---------------------- widgets ------------------------ 
name = tkinter.Entry(input_frame, text="Enter your name", width=20)
submit_button = tkinter.Button(input_frame, text="Submit", command=submit_name)
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

# ---------------------- create radio buttons for text display -----------------------
case_style = tkinter.StringVar()
case_style.set('normal')
normal_button = tkinter.Radiobutton(
    input_frame, text="Normal Case", variable=case_style, value="normal")
upper_button = tkinter.Radiobutton(
    input_frame, text="Upper Case", variable=case_style, value="upper")
normal_button.grid(row=1, column=0, padx=2, pady=2)
upper_button.grid(row=1, column=1, padx=2, pady=2)

# -------------------- windows mainloop ---------------------------
root.mainloop()
