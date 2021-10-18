# Importing Tkinter
from tkinter import *

# calling the root function and assigin it to tk()
root = Tk()

# Creating a label for the root widget
''' As python is object oriented we can 
write the code as follow OR
like the commented few lines in the second paragraph
But the downside for this approach is the code readability 
as with more complicated GUI you will need many methods
'''
my_label1 = Label(root, text="Hello World!").grid(row=0, column=0)
my_label2 = Label(root, text="I am Kareem...").grid(row=1, column=5)
my_label3 = Label(root, text="                   ").grid(row=1, column=1)
# packing the label to the screen of the app
#my_label1.grid(row=0, column=0)  # top left corner
#my_label2.grid(row=1, column=5)  # the text to the right
#my_label3.grid(row=1, column=1)  # created an empty column in the middle with this many space string


# Creating the event loop on the root widget

root.mainloop()


