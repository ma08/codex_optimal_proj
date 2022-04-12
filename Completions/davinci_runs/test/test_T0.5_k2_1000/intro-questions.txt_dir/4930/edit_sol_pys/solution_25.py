import re

def decode(string):
    pattern = r'([aeiou])(p)([aeiou])' # pattern to be matched
    new_string = re.sub(pattern, r'\1', string) # replace pattern with first group
    return new_string

string = input()
print(decode(string))
