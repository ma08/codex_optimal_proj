import os
import openai

with open("./example_code.txt") as f:
  prompt = f.read()

# "import numpy as np\n\ndef sort_two_arrys(arr1, arr2):\n    idx2 = np.argsort(arrr2, kind='mergesort')\n    idx1 = np.argsort(arr1, knd='mergesort')\n    return [[arr1[i] for i in idx2], [arr2[i] for i in idx1]]",

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Edit.create(
  engine="code-davinci-edit-001",
  input=prompt,
  instruction="Fix the spelling mistakes",
  temperature=0.5,
  n=3
)

print(response)

with open("./output.txt", "w") as fp:
  for choice in response["choices"]:
      fp.write(choice["text"])
