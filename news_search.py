import requests
import urllib.parse
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os

news = []

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

def createArticles(window):
    global news

    yCoord = 200
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

def createWindow():

        # def searchNews():
        #     global newQuery
        #
        #     getData(newQuery)
        #     createArticles()

        window = Tk()

        entry = Entry(window)
        entry.place(x=200,y=30)

        newQuery = entry.get()

        window.title("Phrog")
        window.geometry("1440x900")

        path = "Images/logo.png"
        img = ImageTk.PhotoImage(Image.open(path))
        logo = Label(window, image = img)
        logo.place(x=10,y=30)


        # createArticles()

        return window

if __name__== "__main__":

    window = createWindow()
    window.mainloop()
