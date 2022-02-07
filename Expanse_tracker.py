from tkinter import *
from tkcalendar import Calendar

if __name__ == '__main__':
    root = Tk()
    
    item = []
    items = [['Type','Name','Date','Amount']]

    cal = Calendar(root, selectmode = 'day', year = 2022, month = 2, day = 5)
    cal.config()
    cal.grid(row = 4, column = 1)
    
    def getdate():
        date_entry.delete(first=0, last=8)
        date_entry.insert(END, cal.get_date())
        

    root.geometry("800x600")

    def del_item(i):
        items.pop(i)
        for j in range(0,4):
            e = Entry(root, width=15, font=("Courrier",11))
            e.grid(row=i+7, column=j)

    def tables(lst):
        total_rows = len(lst)
        total_columns = len(lst[0])
        for i in range(total_rows):
            for j in range(total_columns):
                  
                e = Entry(root, width=15,
                               font=('Courrier',11))
                e.grid(row=i+7, column=j)
                e.insert(END, lst[i][j])
            if i>0:
                delete = Button(root, text='X',width = 5)
                delete.config(command=lambda: del_item(i))
                delete.grid(row=i+7,column=j+1)
    def add():
        acceptable_types = ['debit','credit','cash']
        if type_input.get().lower() in acceptable_types :
            type_input.config(background="white")
            item = [type_input.get(), name_input.get(), date_entry.get(),amount_input.get()]
            items.append(item)
            print(items)
            tables(items)
            date_entry.delete(first=0, last=len(date_entry.get()))
            name_input.delete(first=0, last=len(name_input.get()))
            type_input.delete(first=0, last=len(type_input.get()))
            amount_input.delete(first=0, last=len(amount_input.get()))
        else:
            type_input.config(background="red")
            type_input.delete(first=0, last=len(type_input.get()))
            type_input.insert(END, "Specify if it is debit, cash or credit")

    def callback_Type(input):
        if input.isnumeric():
            return False
        elif input == "":
            return True
        else:
            return True
    
    def callback_amount(input):
        if input.isnumeric():
            return True
        elif input == "":
            return True
        else:
            return False

    reg_type = root.register(callback_Type)
    reg_amount = root.register(callback_amount)
    ## app label
    app_label = Label(root, text="Expense Tracker")
    app_label.config(font=("Courrier", 18))
    app_label.grid(row=0, column= 2)
    ## task label
    task_label = Label(root, text="Add A New Item: ")
    task_label.config(font=("Courrier",14))
    task_label.grid(row=1, column=2)
    ## NAME INPUT
    name_label = Label(root, text='Name')
    name_label.config(font=("Courrier", 14))
    name_label.grid(row=2, column=0)
    name_input = Entry(root, width=20)
    name_input.config(font=("Courrier",11))
    name_input.grid(row=2, column=1)
    ## TYPE INPUT
    type_label = Label(root, text= "Type")
    type_label.config(font=("Courrier", 14))
    type_label.grid(row=2, column=2)
    type_input = Entry(root, width=20)
    type_input.config(font=("Courrier",11))
    type_input.grid(row=2, column=3)
    type_input.config(validate='key', validatecommand=(reg_type, '%P'))
    ## Date INPUT
    date_label = Label(root, text= "Date")
    date_label.config(font=("Courrier", 14))
    date_label.grid(row=3, column=0)
    date_input = Button(root, text='get date', width=20)
    date_input.grid(row=5, column=1)
    date_input.config(command=getdate)
    date_entry = Entry(root, width=20)
    date_entry.config(font=("Courrier",11))
    date_entry.grid(row=3, column=1)
    ## Amount INPUT
    amount_label = Label(root, text = "Amount")
    amount_label.config(font = ("Courrier", 14))
    amount_label.grid(row = 3, column = 2)
    amount_input = Entry(root, width = 20)
    amount_input.config(font=("Courrier", 11))
    amount_input.grid(row=3, column=3)
    amount_input.config(validate='key', validatecommand=(reg_amount, '%P'))
    ## Add item
    add_item = Button(root, text="Add Item", command=add)
    add_item.grid(row=3, column=4)
    ## Table
    table_label = Label(root, text="Item Table")
    table_label.config(font=("Courrier",14))
    table_label.grid(row=6)
    root.mainloop()


