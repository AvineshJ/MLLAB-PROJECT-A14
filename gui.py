import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import os
import subprocess
from Program import nameyou
import Program
root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=500)
canvas.grid(columnspan=12, rowspan=12)

#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=2)

#instructions
instructions = tk.Label(root, text="Select a number plate of car and find whether it is allowed to enter or not", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1,padx=10,pady=10)

def open_file():
    browse_text.set("COMPLETED")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("jpeg file", "*.jpeg")])
#run program
def run():
    os.system('python Program.py')
def output():
    if res!=-1:
        e_label = tk.Label(root, text= "The vehicle is allowed to enter",font="Raleway", fg="Green",height=2,width=28)
        e_label.grid(columnspan=1,column=3, row=2)
    else:
        e_label = tk.Label(root, text= "The vehicle is not allowed to enter",font="Raleway", fg="red",height=2,width=28)
        e_label.grid(columnspan=1, column=3, row=2)
#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=20)
browse_text.set("SELECT THE IMAGE")
browse_btn.grid(column=1, row=3,padx=10,pady=10)
#run button
btn = tk.Button(root, text="Run the program",font="Raleway", bg="#20bebe", fg="white",height=2,width=20,command=run)
btn.grid(column=1, row=4,padx=10,pady=10)
#status label
a_label=tk.Label(root,text="STATUS",font="Raleway", bg="red", fg="white", height=2, width=10)
a_label.grid(rowspan=2,column=2,row=1)
canvas = tk.Canvas(root, width=1000, height=500)
canvas.grid(columnspan=12,rowspan=12)
res=Program.result
#nameyou(res)
btn = tk.Button(root, text="output",font="Raleway", bg="#20bebe", fg="white",height=2,width=20,command=output)
btn.grid(column=1, row=5)
root.mainloop()





