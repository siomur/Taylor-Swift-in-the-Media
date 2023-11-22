import pandas as pd
import string
from collections import Counter

def get_categories(filename):
    df = pd.read_csv(filename,sep = '\t')

    categories = df['topic'].unique()

    for category in categories:

        entries_in_category = df[df['topic'] == category]['content'].tolist()

    for entry in entries_in_category:
        with open(f'{category}.txt','w') as output:
            output.write(entry)

def get_most_common_words(filename, num_words):
    # Read the text from the file
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # Remove punctuation and split the text into words
    translator = str.maketrans("", "", string.punctuation)
    words = text.translate(translator).split()

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Get the most common words
    most_common_words = word_counts.most_common(num_words)

    return most_common_words

# Replace 'your_document.txt' with the path to your text document
#most_common_words = get_most_common_words(filename, 10)

# Print the most common words and their frequencies
#for word, count in most_common_words:
#    print(f'{word}: {count}')