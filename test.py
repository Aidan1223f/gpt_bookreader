import pdf_reader
import lookup
import gpt
import requests
import pdf_reader 


r = requests.get(r'https://www.gutenberg.org/cache/epub/64317/pg64317.txt')
great_gatsby = r.text

chunks = pdf_reader.chunk_words(great_gatsby)
print("Welcome to GPT bookreader, I can answer any question you have on a book")

question = ""
limit = 5

while question.lower() != "quit" or "exit":
    question = input("GPT: what do you want to know?\nYou: ")
    print()

    keywords = gpt.get_keywords(question)
    print("searching: " + ", ".join(keywords))

        #quit button
    if question.lower() ==  "quit" or "exit":
        "BYE. thank u!"
        
    matches = lookup.find_matches(chunks, keywords)
    
    print(matches)
    for i, chunk_id in enumerate(matches.keys()):
        chunk = chunks[chunk_id]
        response = gpt.answer(chunk, question)

        if response.get("answer_found"):
            print(str((response.get("response"))))
            break
        
        if limit > 5:
            break

    if not response.get("answer_found"):
        print("GPT: sorry I cannot find the answer to that question.")
        

#
    
