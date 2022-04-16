import re

with open("input.txt", "r") as f:
    data = f.read()
    print(data)
    print(re.sub(r'[^\w\s]','',data))



