
import re

def decode(string):
    new_string = re.sub(r'([aeiou])(p)(\1)', r'\1', string)
    return new_string

string = input()
print(decode(string))
