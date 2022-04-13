

import sys, math

def multigram(s):
    if len(s) % 2 == 1: # multigram is a word that can be split into two equal parts
        return -1
    else:
        half = len(s) // 2
        first = s[:half]
        second = s[half:]
        first_letters = {}
        second_letters = {}
        for letter in first:
            if letter in first_letters:
                first_letters[letter] += 1
            else:
                first_letters[letter] = 1
        for letter in second:
            if letter in second_letters:
                second_letters[letter] += 1
            else:
                second_letters[letter] = 1
        for key in first_letters:
            if key not in second_letters:
                return -1
            elif first_letters[key] != second_letters[key]:
                return -1
        return first

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def is_palindrome(s):
    return s == s[::-1]

def find_palindrome(n):
    while not is_palindrome(str(n)):
        n += 1
    return n

def main():
    s = sys.stdin.readline().strip()
    print(is_prime(int(s)))

if __name__ == "__main__":
    main()
