import requests
import urllib.parse

word = 'a lot'
apiKey = '4fb83061-a516-42d4-ab2f-b35b8f73af2b'
mainApi = 'https://dictionaryapi.com/api/v3/references/collegiate/json/'

url = mainApi + urllib.parse.quote(word) + "?key=" + apiKey

print(url)

data = requests.get(url).json()[0]

print(data)
