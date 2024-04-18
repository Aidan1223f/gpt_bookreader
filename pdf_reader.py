
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


# print(tokenized_text)