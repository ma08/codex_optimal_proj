import re

def decode(string):
    pattern = r'([aeiou])(p)(\1)'  # pattern to match
    new_string = re.sub(pattern, r'\1', string)
    return new_string  # return new string

string = input()
print(decode(string))
