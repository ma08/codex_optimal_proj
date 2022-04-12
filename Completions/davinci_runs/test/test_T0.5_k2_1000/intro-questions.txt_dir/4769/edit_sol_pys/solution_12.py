

import sys

def multigram(s): # multigram = multi + anagram
    if len(s) % 2 == 1:
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
        return first, second

def main():
    s = sys.stdin.readline().strip()
    first, second = multigram(s)
    print(first, second)

if __name__ == "__main__":
    main()
