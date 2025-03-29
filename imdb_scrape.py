import requests


title = "The Matrix"
parameters = {"t": title, "apikey": 'bcbfd86f'}
response = requests.get("http://www.omdbapi.com/", parameters)
data = response.json()

print(data)