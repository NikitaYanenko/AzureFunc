import requests

url = "https://doubleconsonants.azurewebsites.net/api/doubleconsonants"
data = {"text": "Hello world!"}

response = requests.post(url, json=data)
print(response.text)
