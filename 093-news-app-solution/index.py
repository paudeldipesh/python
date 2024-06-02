import json

import requests

query = input("What kind of news do you find most informative: ")
API_KEY = "a384d0dd2a2a4d05a5fb8803de662523"
API_URL = f"https://newsapi.org/v2/everything?q={query}&from=2024-05-02&sortBy=publishedAt&apiKey={API_KEY}"

response = requests.get(API_URL)
news_info = json.loads(response.text)

new_news_list = []
for article in news_info["articles"]:
    data = {
        "title": article["title"],
        "description": article["description"],
    }
    new_news_list.append(data)
print(new_news_list)
