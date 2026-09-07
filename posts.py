import requests


url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()
# print(data)

for i in data:
    print(i)
