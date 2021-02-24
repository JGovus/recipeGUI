from tkinter import *

root = Tk()



def hide():
    ingredient_frame.grid_forget()
    ingredient_frame = Frame(root, height=500, width=1000, bg="blue", bd=1, command=hide)
    ingredient_frame.grid(row=7, column=0, padx=20, columnspan=6)