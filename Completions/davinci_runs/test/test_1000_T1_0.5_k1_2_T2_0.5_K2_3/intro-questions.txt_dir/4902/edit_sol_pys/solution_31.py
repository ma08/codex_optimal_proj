
#Solution

#!/usr/bin/python

def is_palindrome(word):
    return word == word[::-1]

def get_palindromes(word):
    word = word.lower()
    word_dict = {}
    for char in word:
        if char in word_dict:
            word_dict[char] += 1
        else:
            word_dict[char] = 1

    odd_count = 0
    for count in word_dict.values():
        if count % 2 == 1:
            odd_count += 1
    return odd_count - 1 if odd_count else 1

word = input()
print(get_palindromes(word))
