import openai
openai.api_key = "sk-1VowbNHFv..."
completion = openai.Completion.create(engine="gpt-3.5-turbo",
                         prompt="¿Que es ChatGPT?.",
                         mat_totokens = "2048")

print(completion.choices[0].text)
