import json
import csv 
import requests

def get_articles(n,apiKey):

    # Define the NewsAPI URL
    url = 'https://newsapi.org/v2/everything'

    # Parameters for the API request
    params = {
        'apiKey': apiKey,
        'language': 'en',
        'q' : "Taylor Swift",
    }

    # Send the API request
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        return articles[:n]
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")
        return []
    
#Need the title, content, date published
def article_to_tsv(apiKey):

    articles = get_articles(500,apiKey)

    with open("taylor.tsv",'w', newline = '', encoding = 'utf-8') as tsv_file:
        writer = csv.writer(tsv_file, delimiter = '\t')

        writer.writerow(['Title','Content','Publish Date'])
        
        for article in articles:
             writer.writerow([article['title'], article['content'], article['publishedAt']])

article_to_tsv('3c3c117c4f2f4fffa6bcf4f877544e2a')