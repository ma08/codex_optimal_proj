import re

p = re.compile("^[0-9]*$")

while True:
    s = input()
    if p.match(s):
        break
    else:
        print("Enter a numeric value")

print(int(s) * 2)
