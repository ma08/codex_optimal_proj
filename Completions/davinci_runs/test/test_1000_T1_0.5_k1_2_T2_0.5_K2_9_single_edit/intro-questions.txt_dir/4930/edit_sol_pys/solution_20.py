import sys

import re

def decode(string):
    pattern = r'([aeiou])(p)(\1)'  # word that matches the pattern
    new_string = re.sub(pattern, r'\1', string)  # replace pattern with first group
    return new_string  # return the new string

string = sys.stdin.read()  # read from stdin
print(decode(string))  # print the new string
