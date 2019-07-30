from tkinter import*
import tkinter as tk
from random import *
from tkinter import messagebox
from os import *
from PIL import Image
window = Tk()
window.title("PHROG")
window.geometry("1440x900")
window.configure(background = 'grey')

path ="SLAB.png"
img = PhotoImage(Image.open(path))
panel = Label(window, image = img)
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
