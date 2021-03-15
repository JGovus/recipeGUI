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
#treetime["columns"] = ("Ingredient")

# Column dimensions
#treetime.column("#0", width=10, minwidth=1)
#treetime.column("Ingredient", width=120, minwidth=25)



# Column heading
#treetime.heading("#0", text="", anchor=W)
#treetime.heading("Ingredient", text="Name", anchor=W)


# Create rows
#Row1 = treetime.insert("", 1, text="1", values=("B1","C1"))


# Add Data


def load_treetime():
    treetime['columns'] = ("ingredient_id", "ingredient_name", "ingredient_type")
    # Format Columns
    treetime.column("#0", width=0, stretch=NO)
    treetime.column("ingredient_id", anchor=W, width=90)
    treetime.column("ingredient_name", anchor=W, width=200)
    # Format Headings
    treetime.heading("#0")
    treetime.heading("ingredient_id", text="Ingredient ID", anchor=W)
    treetime.heading("ingredient_name", text="Ingredient Name", anchor=W)
    # display options
    treetime['displaycolumns'] = "ingredient_name"  # only display one column - still keeping id column
    treetime['show'] = "headings"  # this fixes the resize issue

    c.execute("SELECT * from ingredients ORDER BY ingredient_name DESC")
    ingredients = c.fetchall()

    treetime.grid(row=1, column=0, pady=20, padx=20, rowspan=2)

    count = 0
    for ingredient in ingredients:
        treetime.insert(parent='', index='end', iid=count, text="", values=(ingredient[0], ingredient[1]))
        count += 1


def remove_records_treeview():
    for record in treetime.get_children():
        treetime.delete(record)


load_treetime()


# count
global count
#count=0
#for record in data:
    #treetime.insert(parent='', index='end', iid=count, text="", values=(record[0]))
    #count += 1


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

    ingredient_name = ingredient_box.get()
    sql = '''INSERT INTO ingredients (ingredient_name)
        VALUES(?)'''
    print(ingredient_name)
    c.execute(sql, [ingredient_name])
    conn.commit()
    conn.close()
    ingredient_box.delete(0, END)
    load_treetime()


# delete command
def remove_one(ingredient_id):
    '''x = treetime.selection()[0]
    treetime.delete(x)
    ingredient_name = ingredient_box.get()
    print(ingredient_name)'''
    response = messagebox.askquestion('Are you sure you want to Delete?', "Do you want to Delete?")
    print(ingredient_id, response)
    if response == "yes":
        sql = '''DELETE from ingredients WHERE ingredient_id = ?'''
        c.execute(sql, [ingredient_id])
        conn.commit()
        conn.close()
        ingredient_box.delete(0, 'end')
    load_treetime()


def select_record():
    ingredient_box.delete(0, END)

    selected = treetime.focus()
    values = treetime.item(selected, 'values')
    ingredient_id = values[0]
    ingredient_box.insert(0, values[1])

    update_button = Button(root, text="update", command=lambda: update_record(ingredient_id))
    update_button.grid(column=0, row=1, pady=10)

    delete_button = Button(root, text="delete", command=lambda: remove_one(ingredient_id))
    delete_button.grid(column=0, row=1, pady=10)


def update_record(ingredient_id):
    #selected = treetime.focus()
    #treetime.item(selected, text="", values=(ingredient_box.get()))
    ingredient_name = ingredient_box.get()
    sql = '''UPDATE ingredients SET ingredient_name = ? WHERE ingredient_id = ?'''
    c.execute(sql, [ingredient_name, ingredient_id])
    conn.commit()
    ingredient_box.delete(0, END)
    remove_records_treeview()
    load_treetime()


# button
add_record = Button(root, text="add", command=add_record)
add_record.pack(pady=20)

select_record = Button(root, text="select", command=select_record)
select_record.pack(pady=10)



root.mainloop()
