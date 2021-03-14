from tkinter import *
from tkinter import ttk
from Database import *
from tkinter import messagebox

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
Row1 = treetime.insert("", 1, text="1", values=("B1","C1"))


# Add Data
data = [
]


# count
global count
count=0
for record in data:
    treetime.insert(parent='', index='end', iid=count, text="", values=(record[0]))
    count += 1


treetime.pack(pady=20)


# add entry
# new frame
add_frame = Frame(root)
add_frame.pack(pady=20)

nl = Label(add_frame, text="Ingredient")
nl.grid(row=0, column=0)


# entry box

ingredient_box = Entry(add_frame)
ingredient_box.grid(row=1, column=0)


# add command
def add_record():
    global count
    treetime.insert(parent='', index='end', iid=count, text="", values=(ingredient_box.get()))
    count += 1

    ingredient_box.delete(0, END)

    ingredient_name = ingredient_box.get()
    sql = '''INSERT INTO ingredients (ingredient_name)
        VALUES(?)'''
    c.execute(sql, [ingredient_name])
    conn.commit()
    conn.close_all()


def remove_records_treetime():
    treetime.delete(record)


# delete command
def remove_one():
    x = treetime.selection()[0]
    treetime.delete(x)
    ingredient_name = ingredient_box.get()
    response = messagebox.askquestion('Are you sure you want to Delete?', "Do you want to Delete?")
    print(ingredient_name, response)
    if response == "yes":
        sql = '''DELETE from ingredients WHERE ingredient_id = ?'''
        c.execute(sql, [ingredient_name])
        conn.commit()
        conn.close()
        ingredient_name.delete(0, 'end')


def select_record():
    ingredient_box.delete(0, END)

    selected = treetime.focus()
    values = treetime.item(selected, 'values')

    ingredient_box.insert(0, values[0])


def update_record():
    selected = treetime.focus()
    treetime.item(selected, text="", values=(ingredient_box.get()))
    ingredient_name = ingredient_box.get()
    sql = '''UPDATE ingredients SET ingredient_name = ? WHERE designer_id = ?'''
    c.execute(sql, [ingredient_name])
    conn.commit()
    conn.close()
    ingredient_box.delete(0, END)


# button
add_record = Button(root, text="add", command=add_record)
add_record.pack(pady=20)

select_record = Button(root, text="select", command=select_record)
select_record.pack(pady=10)

update_record = Button(root, text="update", command=update_record)
update_record.pack(pady=10)

delete_record = Button(root, text="delete", command=remove_one)
delete_record.pack(pady=10)


root.mainloop()
