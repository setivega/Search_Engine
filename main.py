import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("Phrog")
window.geometry("1440x900")
window.configure(background='grey')

path = "Super.png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()

# theLabel.mainloop()
# def setup():
#     global picList,img,img2,img3,index,user,onScreen,keyboard,j
#     size(1440,900)
#     img = loadImage("SLAB.jpg")
#     img2 = loadImage("GGB.jpg")
#     img3 = loadImage("PHROG.jpg")
#     user = " "
#     picList = [img, img2, img3]
#     index = int(randint(0, len(picList)-1))
#     background(picList[index])
