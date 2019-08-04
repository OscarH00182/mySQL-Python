import mysql.connector #Allows Python to connect to mySQL
from tkinter import * #For UI
import tkinter as tk #For
from tkinter import ttk #For Database UI
from tkinter import messagebox

myDataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="19724n",
    database="sunglasses"
)

myCursor = myDataBase.cursor()
root = Tk() #tkinter class we import, created a blank window

def entryInput(event):

    newWindow = Toplevel(root) #Creates a new Window
    newWindow.geometry('200x150')#Size of window
    display = Label(newWindow,text = "\nEnter Brand (8 Letters MAX): ",font="Times")
    display.pack() #.pack() is a geometry manager packer
    entry = Entry(newWindow) #Allows for new user to enter value
    entry.pack()
    buttonAction = Button(newWindow, height=1, width=10, text="E N T E R",command=lambda: createRow(entry),font="Times")#Makes button, sends entry to function
    buttonAction.pack()
    mainloop()

def createRow(entry):

    inputValue = entry.get()[:8]#Limits entry to only be MAX 8 characteres long
    mySQLCommand = "INSERT INTO brands (name,top_shelf, bottom_shelf,backstock, clearance, total ) VALUES (%s, %s, %s, %s, %s, %s)" #creates new space for brand
    brand = (inputValue,0,0,0,0,0) #Sets defaults for new brand, INSERTS value passed as brand
    myCursor.execute(mySQLCommand, brand)#executes mySQL code and sets default
    myDataBase.commit()#saves to database
    update()

def entryUpdateInput(event):

    newWindow = Toplevel(root) #Creates a new Window
    newWindow.geometry('200x150')
    lab = Label(newWindow,text = "\nEnter Brand (8 Letters MAX): ",font="Times")
    lab.pack() #.pack() is a geometry manager packer
    entry = Entry(newWindow) #Allows for new user to enter value
    entry.pack()
    buttonAction = Button(newWindow, height=1, width=10, text="E N T E R",command=lambda: UpdateRow(entry),font="Times")
    #command=lambda: UpdateRow() just means do this when I press the button
    buttonAction.pack()
    mainloop()

def UpdateRow(entry):

    newWindow = Toplevel(root)  # Creates a new Window
    newWindow.geometry('200x275')

    textOne = Label(newWindow, text="\nEnter Top Shelf: ",font="Times")
    textOne.pack()  # .pack() is a geometry manager packer
    entryOne = Entry(newWindow)  # Allows for new user to enter value
    entryOne.pack()

    textTwo = Label(newWindow, text="\nEnter Bottom Shelf: ",font="Times")
    textTwo.pack()
    entryTwo = Entry(newWindow)  # Allows for new user to enter value
    entryTwo.pack()

    textThree = Label(newWindow, text="\nEnter Backstock: ",font="Times")
    textThree.pack()
    entryThree = Entry(newWindow)  # Allows for new user to enter value
    entryThree.pack()

    textFour = Label(newWindow, text="\nEnter Clearance: ",font="Times")
    textFour.pack()
    entryFour = Entry(newWindow)  # Allows for new user to enter value
    entryFour.pack()

    buttonAction = Button(newWindow, height=1, width=10, text="E N T E R", command=lambda: calculate(entryOne,entryTwo,entryThree,entryFour,entry,),font="Times")
    buttonAction.pack()
    mainloop()

def calculate(entryOne,entryTwo,entryThree,entryFour,entry):

    brand = entry.get()
    topsh = entryOne.get()
    botsh = entryTwo.get()
    backsk = entryThree.get()
    clear = entryFour.get()
    totalSum = int(topsh) + int(botsh) + int(backsk) + int(clear)

    mySQLCommand = "UPDATE brands SET top_shelf = %s, bottom_shelf = %s, backstock = %s, clearance = %s,total = %s WHERE name = %s "
    myCursor.execute(mySQLCommand,(topsh,botsh,backsk,clear,totalSum,brand,))
    myDataBase.commit()
    update()

def entryDelete(event):

    newWindow = Toplevel(root) #Creates a new Window
    newWindow.geometry('200x150')
    text = Label(newWindow,text = "\nEnter Brand (8 Letters MAX): ",font="Times")
    text.pack() #.pack() is a geometry manager packer
    entry = Entry(newWindow) #Allows for new user to enter value
    entry.pack()
    buttonAction = Button(newWindow, height=1, width=10, text="D E L E T E", command=lambda:deleteRow(entry))
    buttonAction.pack()
    mainloop()

def deleteRow(entry):
    inputValue = entry.get()[:8]
    brandName = (inputValue,)
    myCursor.execute("SELECT * FROM brands WHERE name = %s",brandName)
    searchValue = myCursor.fetchone()

    if(searchValue == None):#Checks if value is in database if not
        retry()#Please try again
    else:#If found, it deletes it
        confirmation(brandName)
        
def retry():

    newWindow = Toplevel(root)
    newWindow.geometry('200x150')
    text = Label(newWindow,text="\n\n\nItem doesn't exist...\n Please Exit, and try again!\n",font="Times")
    text.pack()

def confirmation(brandName):

    messagebox = tk.messagebox.askquestion('Inventory Deletion', 'Are you sure you want to delete this item?',icon='warning')
    if messagebox == 'yes':
        valueDelete = "DELETE FROM brands WHERE name = %s"
        myCursor.execute(valueDelete, brandName)
        myDataBase.commit()
        update()
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the Main Menu')
    root.mainloop()


def previewDataBase(event):

    root = tk.Tk()
    myCursor.execute("SELECT name,top_shelf, bottom_shelf, backstock, clearance,total FROM brands")
    resultData = myCursor.fetchall()
    text = tk.Label(root, text="Current Inventory DataBase", font=("Times",20)).pack()
    columns = ('#','Brand', 'Top Shelf', 'Bottom Shelf', 'Back Stock', 'Clearance', 'Total')
    listBox = ttk.Treeview(root, columns=columns, show='headings')

    for i, ( brand, topshelf, bottom, backstock,clearance,total ) in enumerate(resultData, start=1):
        listBox.insert("", "end", values=(i,brand, topshelf, bottom, backstock,clearance,total))#insert value to sheet

    for col in columns:
        listBox.heading(col, text=col)
    listBox.pack()
    root.mainloop()

def update():

    newWindow = Toplevel(root)
    newWindow.geometry('200x150')
    text = Label(newWindow,text="\n\n\n\nDatabase has been UPDATED\n",font="Times")
    text.pack()
