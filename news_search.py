import requests
import urllib.parse
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os

news = []
newQuery = ''

def hit():
    global query
    os.system('python3 news_search.py')
    getData(query)


def getData(query):
    global news

    print("Query: ",query)
    apiKey = '5ed40e8e488f4b26a289403dd6c181ef'
    mainApi = 'https://newsapi.org/v2/everything?'

    params = {'q': query, 'apiKey': apiKey}
    url = mainApi + urllib.parse.urlencode(params)

    data = requests.get(url).json()

    articles = data['articles']

    for article in articles:
        newsArticle = {}
        newsArticle['name'] = article['source']['name']
        newsArticle['title'] = article['title']
        newsArticle['description'] = article['description']
        newsArticle['url'] = article['url']
        newsArticle['image'] = article['urlToImage']

        news.append(newsArticle)

    print(news)
    print(len(news))

def createArticles(window):
    global news

    yCoord = 50
    for article in news:
        titleLabel = Label(window, text = article['title'], fg = 'blue', font = (None,20))
        titleLabel.place(x = 200,y = yCoord)
        nameLabel = Label(window, text = article['name'],  fg = 'green', font = (None,15))
        nameLabel.place(x = 200,y = yCoord+30)
        descriptionLabel = Label(window, text = article['description'], wraplength = 600, justify=LEFT)
        descriptionLabel.place(x = 200,y = yCoord+60)
        yCoord+= 150
    print("Articles Creating")

#This creates the main window of an application

def searchNews():
    global newQuery

    getData(newQuery)
    createArticles(window)



def createWindow():

    window = Toplevel()

    scroll = Scrollbar(window)
    scroll.pack(side=RIGHT, fill =Y)

    listbox = Listbox(window, yscrollcommand = scroll.set)

    scroll.config(command = listbox.yview)

    unlock=Button(window,text="$5.99 to scroll")
    unlock.place(x=1200, y=25)


    window.title("Phrog")
    window.geometry("1440x900")


    return window

if __name__== "__main__":

    window = createWindow()
    path = "Images/logoBig.png"
    img3 = ImageTk.PhotoImage(Image.open(path))
    logo = Label(window, image = img3)
    logo.place(x=10,y=10)
    window.mainloop()
