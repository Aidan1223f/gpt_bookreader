from openai import OpenAI
import json
import os 

client = OpenAI(api_key="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")


def get_keywords(question):
    prompt = f"""please provide me with 10 keywords from the question that will help find an answer.
    only one word per keyword. only use lowercase
    {question}"""

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": prompt,
            }
        ],
        functions=[
            {
                "name" : "list_keywords",
                "description" : "gives user list of keywords",
                "parameters" :{
                    "type":"object",
                    "properties" : {
                        "list":{
                            "type" : "array",
                            "items": {
                                "type":"string",
                                "description": "A keyword"
                            },
                            "description" : "A list of keywords"

                        }
                    }
                },
                "required" : ["list"]
            }
        ],
        function_call={
            "name":"list_keywords",
            "arguments" : ["list"]
        }
        )
        
    arguments = response.choices[0].message.function_call.arguments.lower()
    keywords = json.loads(arguments)["list"]
    return " ".join(keywords).split(" ")


def answer(chunk, question):
    prompt = f"""```
{chunk}
```

Based on the above information, what is the answer to this question?

```
{question}
```"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Always set answer_found to false if the answer to the question was not found in the informaton provided."
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.5
        top_p=0.5
        functions=[
            {
                "name": "give_response",
                "description": "Use this function to give the response and whether or not the answer to the question was found in the text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "answer_found": {
                            "type": "boolean",
                            "description": "Set this to true only if the provided text includes an answer to the question"
                        },
                        "response": {
                            "type": "string",
                            "description": "The full response to the question, if the information was relevant"
                        }
                    }
                },
                "required": ["answer_found"]
            }
        ]
    )

    return json.loads(response.choices[0].message.function_call.arguments)

