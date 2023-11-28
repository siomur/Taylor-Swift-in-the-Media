import json
import pandas as pd
from collections import Counter
import string
import math
import sys

stopwords = ['a', 'about', 'above', 'across', 'after', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'among', 'an', 'and', 'another', 'any', 'anybody', 'anyone', 'anything', 'anywhere', 'are', 'area', 'areas', 'around', 'as', 'ask', 'asked', 'asking', 'asks', 'at', 'away', 'b', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes', 'been', 'before', 'began', 'behind', 'being', 'beings', 'best', 'better', 'between', 'big', 'both', 'but', 'by', 'c', 'came', 'can', 'cannot', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly', 'come', 'could', 'd', 'did', 'differ', 'different', 'differently', 'do', 'does', 'done', 'down', 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'either', 'end', 'ended', 'ending', 'ends', 'enough', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'f', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'find', 'finds', 'first', 'for', 'four', 'from', 'full', 'fully', 'further', 'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally', 'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great', 'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'herself', 'high', 'high', 'high', 'higher', 'highest', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'important', 'in', 'interest', 'interested', 'interesting', 'interests', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kind', 'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 'last', 'later', 'latest', 'least', 'less', 'let', 'lets', 'like', 'likely', 'long', 'longer', 'longest', 'm', 'made', 'make', 'making', 'man', 'many', 'may', 'me', 'member', 'members', 'men', 'might', 'more', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself', 'n', 'necessary', 'need', 'needed', 'needing', 'needs', 'never', 'new', 'new', 'newer', 'newest', 'next', 'no', 'nobody', 'non', 'noone', 'not', 'nothing', 'now', 'nowhere', 'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on', 'once', 'one', 'only', 'open', 'opened', 'opening', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'our', 'out', 'over', 'p', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place', 'places', 'point', 'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting', 'presents', 'problem', 'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 'really', 'right', 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'sees', 'several', 'shall', 'she', 'should', 'show', 'showed', 'showing', 'shows', 'side', 'sides', 'since', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody', 'someone', 'something', 'somewhere', 'state', 'states', 'still', 'still', 'such', 'sure', 't', 'take', 'taken', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'things', 'think', 'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'three', 'through', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'turn', 'turned', 'turning', 'turns', 'two', 'u', 'under', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses', 'v', 'very', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', 'way', 'ways', 'we', 'well', 'wells', 'went', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole', 'whose', 'why', 'will', 'with', 'within', 'without', 'work', 'worked', 'working', 'works', 'would', 'x', 'y', 'year', 'years', 'yet', 'you', 'young', 'younger', 'youngest', 'your', 'yours', 'z']
def get_categories(filename):
    df = pd.read_csv(filename,sep = '\t')

    categories = [ "Taylor Swift: The Eras Tour Movie", "Relationship with Travis Kelce & the NFL","Albums & Songs",
                  "Billionaire Status", "Awards/Award Shows & Records","Performances/Eras Tour","Style/Looks",
                  "Taylor Swift personal life (activities with friends & friendships & past)"]

    final_dict = {}

    for item in categories:

        entries_of_item = df[df['Category'] == item]['Content'].fillna('').tolist()

        character_text = ' '.join(entries_of_item)

        character_text = character_text.translate(str.maketrans('', '', string.punctuation)).lower()
        
        word_counts = Counter(character_text.split())

        filtered_word_counts = {word: count for word, count in word_counts.items() if count >= 3 and word not in stopwords}

        final_dict[item] = filtered_word_counts

    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump(final_dict, json_file, ensure_ascii=False, indent=2)

def compute_tf(w,category):
    with open("output.json",'r') as file:
        data = json.load(file)

        word_count = data.get(category, {}).get(w, 0)
        #getting the word count in given category
        return word_count
    
def compute_idf(w,script):

    with open(script,'r') as file:
        data = json.load(file)

        speakers_with_word = sum(w in speaker for speaker in data.values())
        #creating the idf computer
        return (math.log(6/speakers_with_word))
    
def compute_tfidf(w,category,script):

    tf = compute_tf(w,category)
    idf = compute_idf(w,script)
    #making the tf-idf for a given word
    result = (tf * idf)

    return result

def tfidf_to_json(n,input_file):
    speaker_dict = {}
    #opening the input json
    with open(input_file,'r') as file:
        
        data = json.load(file)
        #for each speaker calculate the tf-idf and then get the top n items
        #create a new dict that contains the words and their corresponding tf-idfs
        for speaker in data:
            word_dict = {}
            for word in data[speaker]:
                
                word_tfidf = compute_tfidf(word,speaker,input_file)
                
                word_dict[word] = word_tfidf

            speaker_dict[speaker] = word_dict

    highest_tfidf_by_speaker = {character: dict(Counter(character_data).most_common(n)) for character, character_data in speaker_dict.items()}
    #dumping into the stdout stream
    with open('tfidf.json', 'w') as file:
        json.dump(highest_tfidf_by_speaker, file)

tfidf_to_json(10,"output.json")

def sentiment_percent(filename):

    df = pd.read_csv(filename, sep = '\t')

    sentiment_count = df["Sentiment"].value_counts()

    total_entries = len(df)
    percentage_positive = (sentiment_count.get('P', 0) / total_entries) * 100
    percentage_negative = (sentiment_count.get('N', 0) / total_entries) * 100
    percentage_neutral = (sentiment_count.get('-', 0) / total_entries) * 100

    # Print the percentages
    print(f'Percentage Positive: {percentage_positive:.2f}%')
    print(f'Percentage Negative: {percentage_negative:.2f}%')
    print(f'Percentage Neutral: {percentage_neutral:.2f}%')

#sentiment_percent("taylor.tsv")

def cat_percent(filename):

    df = pd.read_csv(filename, sep = '\t')

    sentiment_count = df["Category"].value_counts()

    total_entries = len(df)
    cat1 = (sentiment_count.get('1', 0) / total_entries) * 100
    cat2 = (sentiment_count.get('2', 0) / total_entries) * 100
    cat3 = (sentiment_count.get('3', 0) / total_entries) * 100
    cat4 = (sentiment_count.get('4', 0) / total_entries) * 100
    cat5 = (sentiment_count.get('5', 0) / total_entries) * 100
    cat6 = (sentiment_count.get('6', 0) / total_entries) * 100
    cat7 = (sentiment_count.get('7', 0) / total_entries) * 100
    cat8 = (sentiment_count.get('8', 0) / total_entries) * 100
    null = (sentiment_count.get('-', 0) / total_entries) * 100
    

    # Print the percentages
    print(f'Percentage cat1: {cat1:.2f}%')
    print(f'Percentage cat2: {cat2:.2f}%')
    print(f'Percentage cat3: {cat3:.2f}%')
    print(f'Percentage cat4: {cat4:.2f}%')
    print(f'Percentage cat5: {cat5:.2f}%')
    print(f'Percentage cat6: {cat6:.2f}%')
    print(f'Percentage cat7: {cat7:.2f}%')
    print(f'Percentage cat8: {cat8:.2f}%')
    print(f'Percentage null: {null:.2f}%')

#cat_percent("taylor.tsv")
     