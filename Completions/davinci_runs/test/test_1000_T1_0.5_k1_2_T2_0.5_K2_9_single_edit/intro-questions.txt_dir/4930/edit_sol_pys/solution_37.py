
import re

def decode(string):
    pattern = r'([aeiou])([p])\2'
    new_string = re.sub(pattern, r'\1', string, flags=re.IGNORECASE)
    return new_string

string = input()
print(decode(string))
