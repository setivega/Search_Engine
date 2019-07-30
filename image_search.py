import requests
import urllib.parse
import pyunsplash


query = 'dog'

client_id = "628a36f83557e1f662357b63e8d97a5bb2f7086f42c5cb1b325bc44b4617bc13"
mainApi = 'https://api.unsplash.com/search/photos?'
params = {'query': query, 'client_id': client_id}
url = mainApi + urllib.parse.urlencode(params)


print(url)

data = requests.get(url).json()

print(data)

# client_secret = "4aca8fa2142de348dea0eae49dc6fbf141f5b232316ae826a73db76b769a7baa"
# redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
# code = "4a62201d893652b07859659d2dc222ca80a180747a572c3405b70c2b34f4c2b2"

pu = pyunsplash.PyUnsplash(api_key='628a36f83557e1f662357b63e8d97a5bb2f7086f42c5cb1b325bc44b4617bc13')

search = pu.search(type_='photos', query='red car')
for entry in search.entries:
    print(entry.link_html)
