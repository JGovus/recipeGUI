from tkinter import *
from Ingredients import *
root = Tk()
root.title("Weekly Recipes w/ Ingredients")
root.geometry("1200x800")


# Ingredient Frame
def ingredient_frame():
    ingredient_frame = Frame(root, height=500, width=800, bg="blue", bd=1)
    ingredient_frame.grid(row=1, column=0, padx=10, columnspan=6)


#def hide():
 #   ingredient_frame.grid_forget()


#quit_button = Button(ingredient_frame, text="Quit", command=hide())
#quit_button.grid(row=0, column=0)


# Top navigating bar buttons
my_button = Button(root, text="Home", font=("Times New Roman", 12))
my_button.grid(row=0, column=0, padx=0)

my_button1 = Button(root, text="Meals", font=("Times New Roman", 12))
my_button1.grid(row=0, column=1, padx=0)

my_button = Button(root, text="Ingredients", font=("Times New Roman", 12), command=ingredient_frame)
my_button.grid(row=0, column=2, padx=0)

# Week 1-4 buttons
my_button = Button(root, text="Week 1", font=("Times New Roman", 12))
my_button.grid(row=1, column=1, pady=50)

my_button = Button(root, text="Week 2", font=("Times New Roman", 12))
my_button.grid(row=1, column=2, pady=50)

my_button = Button(root, text="Week 3", font=("Times New Roman", 12))
my_button.grid(row=1, column=3, pady=50)

my_button = Button(root, text="Week 4", font=("Times New Roman", 12))
my_button.grid(row=1, column=4, pady=50)

# save options view buttons
my_button = Button(root, text="Save Changes", font=("Times New Roman", 12))
my_button.grid(row=4, column=7, pady=20, sticky=W)

my_button = Button(root, text="Meal Options", font=("Times New Roman", 12))
my_button.grid(row=5, column=7, pady=10, sticky=W)

my_button = Button(root, text="View Shopping Lists", font=("Times New Roman", 12))
my_button.grid(row=6, column=7, pady=10, sticky=W)

# days 1-7 labels
my_label1 = Label(root, text="Day 1", fg="black", font=("Times New Roman", 28))
my_label1.grid(row=2, column=0, columnspan=1, padx=25)

my_label1 = Label(root, text="Day 2", fg="black", font=("Times New Roman", 28))
my_label1.grid(row=2, column=1, columnspan=1, padx=25)

my_label1 = Label(root, text="Day 3", fg="black", font=("Times New Roman", 28))
my_label1.grid(row=2, column=2, columnspan=1, padx=25)

my_label1 = Label(root, text="Day 4", fg="black", font=("Times New Roman", 28))
my_label1.grid(row=2, column=3, columnspan=1, padx=25)

my_label1 = Label(root, text="Day 5", fg="black", font=("Times New Roman", 28))
my_label1.grid(row=2, column=4, columnspan=1, padx=25)

my_label1 = Label(root, text="Day 6", fg="black", font=("Times New Roman", 28))
my_label1.grid(row=2, column=5, columnspan=1, padx=25)

my_label1 = Label(root, text="Day 7", fg="black", font=("Times New Roman", 28))
my_label1.grid(row=2, column=6, columnspan=1, padx=25, pady=40)


# drop down menu options
menu = [
    "Pizza",
    "Asian Chicken and Rice",
    "Chicken and Dumplings",
    "Spaghetti with beef",
    "Pork Chops",
    "Chicken Wings",
    "Tacos",
    "Breakfast for Dinner",
    "Steak and Potatoes",
    "Caesar Salad"
]

# drop down menus for each day
# 1
variable1 = StringVar(root)
variable1.set(menu[0])

w = OptionMenu(root, variable1, *menu)
w.grid(row=3, column=0)

# 2
variable1 = StringVar(root)
variable1.set(menu[1])

w1 = OptionMenu(root, variable1, *menu)
w1.grid(row=3, column=1)

# 3
variable1 = StringVar(root)
variable1.set(menu[0])

w1 = OptionMenu(root, variable1, *menu)
w1.grid(row=3, column=2)

# 4
variable1 = StringVar(root)
variable1.set(menu[0])

w1 = OptionMenu(root, variable1, *menu)
w1.grid(row=3, column=3)

# 5
variable1 = StringVar(root)
variable1.set(menu[0])

w1 = OptionMenu(root, variable1, *menu)
w1.grid(row=3, column=4)

# 6
variable1 = StringVar(root)
variable1.set(menu[0])

w1 = OptionMenu(root, variable1, *menu)
w1.grid(row=3, column=5)

# 7
variable1 = StringVar(root)
variable1.set(menu[0])

w1 = OptionMenu(root, variable1, *menu)
w1.grid(row=3, column=6)


def fake_command():
    pass


# define a menu
my_menu = Menu(root)
root.config(menu=my_menu)
# Create Menu options
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=fake_command)
file_menu.add_command(label='Exit', command=root.quit)







root.mainloop()