#!/usr/bin/env python3

words = []

while True:
    try:
        line = input()
        words.extend(line.split())
    except EOFError:
        break
unique = []
for word in words:
    if word.lower() not in unique: # Check if the word is already in the list
        unique.append(word.lower()) # If not append it
        print(word, end=' ')
    else:
        print('.', end=' ')
print()
