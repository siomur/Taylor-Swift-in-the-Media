import json
import csv 
import requests

def get_articles(n, apiKey, from_date, to_date):

    # Define the NewsAPI URL
    url = 'https://newsapi.org/v2/everything'

    # Parameters for the API request
    params = {
        'apiKey': apiKey,
        'language': 'en',
        'q' : "Taylor Swift",
        'sortBy' : 'relevancy',
        'from' : from_date,
        'to' : to_date
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
def article_to_tsv(apiKey, from_date, to_date):

    articles = get_articles(100,apiKey, from_date, to_date)

    with open("taylor.tsv",'a', newline = '', encoding = 'utf-8') as tsv_file:
        writer = csv.writer(tsv_file, delimiter = '\t')
        
        for article in articles:
             writer.writerow([article['title'], article['content'], article['publishedAt']])



if __name__ == "__main__":

    with open("taylor.tsv",'w', newline = '', encoding = 'utf-8') as tsv_file:
        writer = csv.writer(tsv_file, delimiter = '\t')
        writer.writerow(['Title','Content','Publish Date'])

    article_to_tsv('3c3c117c4f2f4fffa6bcf4f877544e2a', "2023-10-20", "2023-10-25")
    article_to_tsv('3c3c117c4f2f4fffa6bcf4f877544e2a', "2023-10-25", "2023-10-30")
    article_to_tsv('3c3c117c4f2f4fffa6bcf4f877544e2a', "2023-10-30", "2023-11-05")
    article_to_tsv('3c3c117c4f2f4fffa6bcf4f877544e2a', "2023-11-05", "2023-11-10")
    article_to_tsv('3c3c117c4f2f4fffa6bcf4f877544e2a', "2023-11-10", "2023-11-15")