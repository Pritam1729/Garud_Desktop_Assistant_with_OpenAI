import os
import openai
from config import openai_apikey

openai.api_key = openai_apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a c++ code for star pattern",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].text)