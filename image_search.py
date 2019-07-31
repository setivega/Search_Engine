import requests
import urllib.parse

query = 'dog'
client_id = "628a36f83557e1f662357b63e8d97a5bb2f7086f42c5cb1b325bc44b4617bc13"
mainApi = 'https://api.unsplash.com/search/photos?'
params = {'query': query, 'client_id': client_id}
url = mainApi + urllib.parse.urlencode(params)

print(url)

data = requests.get(url).json()

print(data)

results = data['results'][0]
photos = []

print(results)

# def getData(query,):
