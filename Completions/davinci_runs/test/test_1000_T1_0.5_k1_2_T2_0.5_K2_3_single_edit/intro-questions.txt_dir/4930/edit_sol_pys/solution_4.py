
import re

def decode(string):
    pattern = r'([aeiou])(p)(\1)' # this is a regular expression
    new_string = re.sub(pattern, r'\1', string) # r'\1' is the replacement for the pattern
    return new_string

string = input()
print(decode(string))
