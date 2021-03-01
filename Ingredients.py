from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Treeview')
root.geometry("500x600")

#create treeview
treetime = ttk.Treeview(root)

# Create Column
treetime["columns"] = ("Ingredient")

# Column dimensions
treetime.column("#0", width=10, minwidth=1)
treetime.column("Ingredient", width=120, minwidth=25)



# Column heading
treetime.heading("#0", text="", anchor=W)
treetime.heading("Ingredient", text="Name", anchor=W)


# Create rows
#Row1 = treetime.insert("", 1, text="1", values=("B1","C1"))

#Add Data
data = [
    ["pepperoni"],
    ["cheese"]
]


# count
global count
count=0
for record in data:
    treetime.insert(parent='', index='end', iid=count, text="", values=(record[0]))
    count += 1



treetime.pack(pady=20)

#add entry
#new frame
add_frame = Frame(root)
add_frame.pack(pady=20)

nl = Label(add_frame, text="Ingredient")
nl.grid(row=0, column=0)


#entry box

ingredient_box = Entry(add_frame)
ingredient_box.grid(row=1, column=0)

# add command
def add_record():
    global count
    treetime.insert(parent='', index='end', iid=count, text="", values=(ingredient_box.get()))
    count += 1

    ingredient_box.delete(0, END)
# delete command
def remove_one():
    x = treetime.selection()[0]
    treetime.delete(x)

def select_record():
    ingredient_box.delete(0, END)

    selected = treetime.focus()
    values = treetime.item(selected, 'values')

    ingredient_box.insert(0, values[0])




def update_record():
    selected = treetime.focus()
    treetime.item(selected, text="", values=(ingredient_box.get()))
    ingredient_box.delete(0, END)

#button
add_record = Button(root, text="add", command=add_record)
add_record.pack(pady=20)

select_record = Button(root, text="select", command=select_record)
select_record.pack(pady=10)

update_record = Button(root, text="update", command=update_record)
update_record.pack(pady=10)



delete_record = Button(root, text="delete", command=remove_one)
delete_record.pack(pady=10)




root.mainloop()
