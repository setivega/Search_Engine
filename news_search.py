import requests
import urllib.parse
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

query = 'gosh'
apiKey = '5ed40e8e488f4b26a289403dd6c181ef'
mainApi = 'https://newsapi.org/v2/everything?'

params = {'q': query, 'apiKey': apiKey}
url = mainApi + urllib.parse.urlencode(params)

data = requests.get(url).json()

articles = data['articles']

news = []


for article in articles:
    newsArticle = {}
    newsArticle['name'] = article['source']['name']
    newsArticle['title'] = article['title']
    newsArticle['description'] = article['description']
    newsArticle['url'] = article['url']
    newsArticle['image'] = article['urlToImage']

    news.append(newsArticle)

print(news)

def createArticles():
    global news
    yCoord = 200
    for article in news:
        titleLabel = Label(window, text = article['title'])
        titleLabel.place(x = 200,y = yCoord)
        nameLabel = Label(window, text = article['name'])
        nameLabel.place(x = 200,y = yCoord+50)
        descriptionLabel = Label(window, text = article['description'])
        # descriptionLabel.config(width = 1400)
        descriptionLabel.place(x = 200,y = yCoord+100)
        yCoord+= 200

#This creates the main window of an application
window = Tk()
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


searchBar = Entry(window)

createArticles()

window.mainloop()
