import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from random import *
import sys
import os

#This creates the main window of an application
window = tk.Tk()
window.title("Phrog")
window.geometry("1440x900")
window.configure(background='grey')

path = "Images/SLAB.png"
path2 = "Images/GGB.png"
path3 = "Images/PHROG.png"
path4 = "Images/space.png"
picList = [path,path2,path3,path4]

path5 = "Images/logoBig.png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
index = (randint(0, len(picList)-1))
img = ImageTk.PhotoImage(Image.open(picList[index]))
img2 = tk.PhotoImage(Image.open(path5))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)
logo1 = tk.Label(window, image = img2)
logo1.place(x=770,y=450)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

def runSearch():
    os.system('python3 news_search.py')

search=tk.Button(window,text="Search",command= runSearch)
search.place(x=10, y=10)

#Start the GUI
window.mainloop()
