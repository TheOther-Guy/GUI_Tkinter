# Importing Tkinter
from tkinter import *

# calling the root function and assigin it to tk()
root = Tk()

# adding the button 
# and notice disabled here make the button unclickable
mybutton = Button(root, text='click me!', state="disabled") 
# packing the Button to the screen 
mybutton.pack()





root.mainloop()