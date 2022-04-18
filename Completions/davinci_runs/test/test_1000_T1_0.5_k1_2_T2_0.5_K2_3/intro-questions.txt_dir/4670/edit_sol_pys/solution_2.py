"""
    Problem Statement:
        You are given a string S.
        Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""

import re

if __name__ == '__main__':
    input_string = input()

    print(any(character.isalnum() for character in input_string))
    print(any(character.isalpha() for character in input_string))
    print(any(character.isdigit() for character in input_string))
    print(any(character.islower() for character in input_string))
    print(any(character.isupper() for character in input_string))
