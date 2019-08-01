import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from random import *
import sys
import os
from news_search import getData, createArticles, createWindow


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
img2 = ImageTk.PhotoImage(Image.open(path5))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)
logo = tk.Label(window, image = img2)
logo.place(x=502,y=104)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

entry = Entry(window)
entry.place(x=600,y=450)

def runSearch():
    global entry

    query = entry.get()
    getData(query)
    window1 = createWindow()
    createArticles(window1)
    window1.mainloop()
    # os.system('python3 news_search.py soccer')

#Start the GUI
window.mainloop()
