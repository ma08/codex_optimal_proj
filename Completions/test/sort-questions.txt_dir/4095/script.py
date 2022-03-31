import openai
import os
import json

with open("./question.txt") as f:
  prompt_r = f.read()

choices_number=3

response = openai.Completion.create(
  engine="code-davinci-002",
  prompt= prompt_r,
  temperature=0.4,
  max_tokens=500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  # stop=stop,
  n=choices_number,
)


json_list=[]
for choice in response.choices:
  json_list.append(choice.text)

with open('solutions1.json','w') as outfile:
  json.dump(json_list,outfile)

