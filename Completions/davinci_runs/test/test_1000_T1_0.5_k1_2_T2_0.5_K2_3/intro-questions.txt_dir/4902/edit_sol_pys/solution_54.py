
#!/usr/bin/env python3

letters = [0 for i in range(26)]

for letter in input():
    letters[ord(letter) - ord('a')] += 1

print(sum(letter % 2 for letter in letters))
