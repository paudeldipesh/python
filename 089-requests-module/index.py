import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.google.com/")
soup = BeautifulSoup(response.text, "html.parser")
title_tag = soup.find("title")
print(title_tag)

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Dipesh Paudel",
    "body": "Professional Developer",
    "userId": 7,
}
headers = {
    "Content-type": "application/json; charset=UTF-8",
}
response = requests.post(url, headers=headers, json=data)
print(response.json())
