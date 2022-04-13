import re

def decode(string):
    pattern = r'([aeiou])([p])([aeiou])'
    new_string = re.sub(pattern, r'\1\3', string)
    return new_string

string = input()
print(decode(string))
