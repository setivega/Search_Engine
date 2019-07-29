import json
import requests

query = raw_input("Search: ")
apikey = "4fb83061-a516-42d4-ab2f-b35b8f73af2b"
url = "https://dictionaryapi.com/api/v3/references/collegiate/json/"+query+"?key="+apikey



r = requests.get(url)

print(r.text)
