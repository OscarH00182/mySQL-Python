from tkinter import *
from DatabaseFunctions import *

text = Label(root,text = "Count Inventory System\n",font=("Times",15)) #We label the page, we put it in (root, "give it a text")
root.geometry('300x250')
text.pack() #pack page together

Option1 = Button(root,text = "Create New Row",font="Times")
Option1.bind("<Button-1>",entryInput)
Option1.pack()

Option2 = Button(root,text = " Update Inventory",font="Times")
Option2.bind("<Button-1>",entryUpdateInput)
Option2.pack()

Option3 = Button(root,text = "Display Database",font="Times")
Option3.bind("<Button-1>",previewDataBase)
Option3.pack()

Option4 = Button(root,text = "Delete Inven Item",font="Times")
Option4.bind("<Button-1>",entryDelete)
Option4.pack()

Option5 = Button(root,text = "Exit",command = quit)
Option5.pack()
root.mainloop() #keeps page in an open loop until you close out


