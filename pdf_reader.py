
import requests
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import tokenizer
import tiktoken

nltk.download('punkt')
nltk.download('wordnet')

r = requests.get(r'https://www.gutenberg.org/cache/epub/64317/pg64317.txt')
great_gatsby = r.text

# remove unwanted new line and tab characters from the text
for char in ["\n", "\r", "\t"]:
    great_gatsby = great_gatsby.replace(char, " ")
    
def tokenize_text(text: str):
    
    # lowercase the text
    text = text.lower()
    
    # remove punctuation and stopwords from text
    english_stop_words = set(stopwords.words('english'))
    text = re.sub(r"[^\w\s]", "", text)

    text = ' '.join([word for word in text.split() if word in english_stop_words])

    return text

tokenized_text = tokenize_text(text = great_gatsby)

def lemmatize_tokens(text):
    
    # initiate lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in text]
    
    # return your lemmatized tokens
    return lemmatized_tokens

lemmatized_tokens = lemmatize_tokens(tokenized_text)


def chunk_words(file, chunk_size=4000, overlap=1000):
    chunks = []
    chunk = ""
    for word in file:
        chunk += word
        while len(chunk) > chunk_size:
            chunks.append(chunk[:chunk_size])
            chunk = chunk[chunk_size-overlap:]

    if len(chunk):
        chunks.append(chunk)
    return chunks





        
   