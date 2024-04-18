import pdf_reader
import lookup
import gpt
import requests
import pdf_reader 



question = "What does this quote in the book The great Gatbsy mean, 'I hope she'll be a fool -- that's the best thing a girl can be in this world, a beautiful little fool.'" 
keywords = gpt.get_keywords(question)
print("searching: " + ", ".join(keywords))

r = requests.get(r'https://www.gutenberg.org/cache/epub/64317/pg64317.txt')
great_gatsby = r.text

print("Chunking pdf /n")

chunks = pdf_reader.chunk_words(great_gatsby)

print("Welcome to GPT bookreader, I can answer any question you have on a book")
while True:
    question = input("GPT: what do you want to know?\nYou")

    matches = lookup.find_matches(chunks, keywords)

    for chunk_id in matches.keys():
        chunk = chunks[chunk_id]
        response = gpt.answer(chunk, question)

        if response.get("answer_found"):
            print("GPT " + str((response.get("response"))))

    if not response.get("answer_found"):
        print("GPT: sorry I cannot find the answer to that question.")
        
    if question.lower() ==  "quit":
        break
    
