import json
import csv 
import requests
from datetime import datetime, timedelta

def get_articles(n, apiKey):

    # Define the NewsAPI URL
    url = 'https://newsapi.org/v2/everything'

    # Parameters for the API request
    params = {
        'apiKey': apiKey,
        'language': 'en',
        'q' : "Taylor Swift OR Eras Tour OR Eras tour movie",
    }

    # Send the API request
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        return articles
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")
        return []