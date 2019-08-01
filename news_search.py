import requests
import urllib.parse
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

window = Tk()

entry = Entry(window)
entry.place(x=200,y=30)
content = entry.get()

query = content

news = []

def getData(query):
    global news

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

def callback(url):
    webbrowser.open_new(url)

# def navBar():



def createArticles():
    global news

    yCoord = 200
    for article in news:
        titleLabel = Label(window, text = article['title'],fg = 'blue', font=(None, 17))
        titleLabel.place(x = 200,y = yCoord)
        nameLabel = Label(window, text = article['name'], fg='green', font=(None, 15))
        nameLabel.bind("<Button-1>", lambda e: callback(article['url']))
        nameLabel.place(x = 200,y = yCoord+30)
        descriptionLabel = Label(window, text = article['description'], wraplength = 600, justify = LEFT, font = (None, 15))
        descriptionLabel.place(x = 200,y = yCoord+60)
        yCoord+= 150

#This creates the main window of an application

window.title("Phrog")
window.geometry("1440x900")
window.configure(background='white')
t = Text()
t.config(wrap = WORD)

logoPath = "Images/logo.png"

logo = ImageTk.PhotoImage(Image.open(logoPath))

panel = Label(window, image = logo)
panel.place(x=20,y=30)
# panel.pack(side="top", fill='both', expand=True, padx=4, pady=4)


createArticles()


window.mainloop()
