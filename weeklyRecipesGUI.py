from tkinter import *

root = Tk()
root.title("Weekly Recipes w/ Ingredients")
root.geometry("1200x800")

my_button = Button(root, text="Home", font=("Times New Roman", 12))
my_button.grid(row=0, column=0, padx = 0)

my_button1 = Button(root, text="Meals", font=("Times New Roman", 12))
my_button1.grid(row=0, column=1, padx = 0)

my_button = Button(root, text="Ingredients", font=("Times New Roman", 12))
my_button.grid(row=0, column=2, padx = 0)

my_label1 = Label(root, text="Day 1", fg="white", bg="black", font=("Times New Roman", 28))
my_label1.grid(row=1, column=0, columnspan=1, padx= 25)

my_label1 = Label(root, text="Day 2", fg="white", bg="black", font=("Times New Roman", 28))
my_label1.grid(row=1, column=1, columnspan=1, padx= 25)

my_label1 = Label(root, text="Day 3", fg="white", bg="black", font=("Times New Roman", 28))
my_label1.grid(row=1, column=2, columnspan=1, padx= 25)

my_label1 = Label(root, text="Day 4", fg="white", bg="black", font=("Times New Roman", 28))
my_label1.grid(row=1, column=3, columnspan=1, padx= 25)

my_label1 = Label(root, text="Day 4", fg="white", bg="black", font=("Times New Roman", 28))
my_label1.grid(row=1, column=4, columnspan=1, padx= 25)

my_label1 = Label(root, text="Day 5", fg="white", bg="black", font=("Times New Roman", 28))
my_label1.grid(row=1, column=5, columnspan=1, padx= 25)

my_label1 = Label(root, text="Day 6", fg="white", bg="black", font=("Times New Roman", 28))
my_label1.grid(row=1, column=6, columnspan=1, padx= 25)

my_label1 = Label(root, text="Day 7", fg="white", bg="black", font=("Times New Roman", 28))
my_label1.grid(row=1, column=7, columnspan=1, padx= 25)

root.mainloop()