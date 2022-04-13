#!/usr/bin/env python3

import sys

def read_input(file):
    # Read input
    f = open(file, 'r', encoding='utf-8')
    N = int(f.readline())
    words = []
    for i in range(N):
        words.append(f.readline().strip())
    f.close()
    return N, words

def num_letters(word):
    # Find the number of letters in a word
    count = 0
    for letter in word:
        if letter.isalpha():
            count += 1
    return count

def name_number(num):
    # Convert a number to a word
    if num == 0:
        return ""
    elif num < 11:
        return ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"][num - 1]
    elif num < 20:
        return ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][num - 11]
    elif num < 100:
        if num % 10 == 0:
            return ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][num // 10 - 2]
        else:
            return name_number(num // 10 * 10) + name_number(num % 10)
    elif num < 1000:
        if num % 100 == 0:
            return name_number(num // 100) + " hundred"
        else:
            return name_number(num // 100) + " hundred and " + name_number(num % 100)
    else:
        return "one thousand"

def print_sentence(N, words):
    # Print the sentence
    sentence = ""
    for i in range(N):
        sentence += words[i]
        if words[i] == "$":
            sentence += " " + name_number(sum([num_letters(word) for word in words]))
        if i < N - 1:
            sentence += " "
    print(sentence)

if __name__ == "__main__":
    N, words = read_input(sys.argv[1])
    print_sentence(N, words)
