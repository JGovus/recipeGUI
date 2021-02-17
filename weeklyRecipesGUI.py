from tkinter import *

root = Tk()
root.title("Weekly Recipes w/ Ingredients")
root.geometry("1200x800")

my_label1 = Label(root, text="Day 1", fg="white", bg="black", font=("Times New Roman", 28))
my_label1.grid(row=0, column=0, columnspan=1)

root.mainloop()