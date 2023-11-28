import matplotlib.pyplot as plt
import pandas as pd


def sentiment_chart():
    # look at sentiment column in data set, and make pie chart with the percentages of postive, negative, neutral
    df = pd.read_csv("taylor.tsv", sep="\t")
    # Change labels from P, N, - to positive, negative, neutral
    df['Sentiment'] = df['Sentiment'].map({'P': 'Positive', 'N': 'Negative', '-': 'Neutral'})
    df = df[df['Category'] != '-']
    # Count the number of articles for each sentiment
    sentiment_counts = df['Sentiment'].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Sentiment Distribution of Articles about Taylor Swift', fontweight='bold')
    plt.show()
    plt.savefig('sentiment_pie_chart.pdf')


def categories_chart():
   # make pie chart with the types of categories
   df = pd.read_csv("full_categories_taylor.tsv", sep="\t") 
   df = df[df['Category'] != '-']
   categories_counts = df['Category'].value_counts()

   plt.figure(figsize=(8, 8))
   # autoct makes sure the percentages are shown, startangle=140 is a stylistic element -- not necessary
   plt.pie(categories_counts, labels=categories_counts.index, autopct='%1.1f%%', startangle=140)
   plt.title('Category Distribution of the Articles about Taylor Swift', fontweight='bold')
   plt.show()
   plt.savefig('category_pie_chart.pdf')


def main():
    #sentiment_chart()
    categories_chart()

if __name__ == "__main__":
    main()