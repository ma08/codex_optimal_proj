import openai


choices_number=3

response = openai.Completion.create(
  engine="code-davinci-001",
  prompt=" ''' Given an array of positive and negative integers, segregate them in linear time and constant space. The output should print all negative numbers, followed by all positive numbers. ''' ",
  temperature=1,
  max_tokens=300,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  # stop=stop,
  n=choices_number,
)


with open("resp.txt",'w',encoding = 'utf-8') as f:
   # f.write("my first file\n")
   for i in range(0,choices_number):
     # f.write("choice {}".format(i))
     resp=response.choices[i]
     f.write("{} ".format(resp))
     f.write("\n")

f.close()

  # responses = ["choice:" + choice.text for choice in response.choices]
  # print(responses)

# response = openai.Classification.create(
#     file="file-jVRliPwwlOx1zYXi3H77vkzq",
#     query="movie is very good",
#     search_model="ada", 
#     model="curie", 
#     max_examples=3
# )

# print(response)
