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
    #plt.show()
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
   #plt.show()
   plt.savefig('category_pie_chart.pdf')

def sentiment_in_categories():
   df = pd.read_csv("full_categories_taylor.tsv", sep="\t") 
   # Map 'P' to 'Positive' and 'N' to 'Negative' in the 'sentiment' column
   df['Sentiment'] = df['Sentiment'].map({'P': 'Positive', 'N': 'Negative', '-':'Neutral'})
   #exclude irrelevant characters
   df = df[df['Category'] != '-']
   df['Category'] = df['Category'].map({'Albums & Songs':'Albums & Songs', 'Awards/Award Shows & Records':'Awards/Records', 'Style/Looks': 'Style/Looks', 'Taylor Swift: The Eras Tour Movie':'The Eras Tour Movie', 'Relationship with Travis Kelce & the NFL':'Travis Kelce & the NFL', 'Taylor Swift personal life (activities with friends & friendships & past)':'Personal Life', 'Billionaire Status':'Billionaire Status', 'Performances/Eras Tour':'Performances/Eras Tour'})
   sentiment_percentages = pd.crosstab(df['Category'], df['Sentiment'], normalize='index') * 100

   plt.figure(figsize=(9, 6))
   bars_pos = plt.bar(sentiment_percentages.index, sentiment_percentages['Positive'], color='green', label='Positive')
   bars_neg = plt.bar(sentiment_percentages.index, sentiment_percentages['Negative'], bottom=sentiment_percentages['Positive'],
                       color='red', label='Negative')
   bars_neu = plt.bar(sentiment_percentages.index, sentiment_percentages['Neutral'],
                       bottom=sentiment_percentages['Positive'] + sentiment_percentages['Negative'], color='grey', label='Neutral')

  
   plt.xticks(sentiment_percentages.index, [label.replace(" ", "\n") for label in sentiment_percentages.index])

   plt.xlabel('Category')
   plt.ylabel('Percentage')
   plt.title('Sentiment Distribution by Category')
   plt.legend(title='Sentiment')

   plt.show()
   plt.savefig("sentiment_per_category.pdf")




def main():
    sentiment_chart()
    categories_chart()
    sentiment_in_categories()

if __name__ == "__main__":
    main()