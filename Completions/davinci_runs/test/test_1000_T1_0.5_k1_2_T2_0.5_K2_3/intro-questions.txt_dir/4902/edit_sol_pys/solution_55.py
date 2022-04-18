
letters = [0 for i in range(26)]

for letter in input():
    letters[ord(letter) - ord('a')] += 1

print(sum(1 for letter in letters if letter % 2))
