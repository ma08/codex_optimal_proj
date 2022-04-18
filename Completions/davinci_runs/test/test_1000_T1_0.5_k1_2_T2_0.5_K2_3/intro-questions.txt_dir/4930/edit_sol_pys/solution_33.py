#!/usr/bin/env python3

import re

def decode(string):
    pattern = r'([aeiou])(p)([aeiou])'  # pattern to match
    new_string = re.sub(pattern, r'\1', string)  # substitute pattern with first match
    return new_string

string = input()
print(decode(string))
