import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from random import *
import main

#This creates the main window of an application
# window = tk.Tk()
# window.title("Phrog")
# window.geometry("1440x900")
# window.configure(background='grey')

def backgroundWindow():
    path = "Images/SLAB.png"
    path2 = "Images/GGB.png"
    path3 = "Images/PHROG.png"
    path4 = "Images/space.png"
    picList = [path,path2,path3,path4]
    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    index = (randint(0, len(picList)-1))
    img = ImageTk.PhotoImage(Image.open(picList[index]))

    # # #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    # panel = tk.Label(window, image = img)
    # #
    # # #The Pack geometry manager packs widgets in rows or columns.
    # panel.pack(side = "bottom", fill = "both", expand = "yes")
    # #Start the GUI
    # window.mainloop()
