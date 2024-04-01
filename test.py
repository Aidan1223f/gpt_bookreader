import pdf_reader
import lookup
import requests

question = "I hope she'll be a fool -- that's the best thing a girl can be in this world, a beautiful little fool." 
keywords = question.split(" ")

r = requests.get(r'https://www.gutenberg.org/cache/epub/64317/pg64317.txt')
great_gatsby = r.text

chunks = pdf_reader.chunk_words(great_gatsby)
matches = lookup.find_matches(chunks, keywords)
