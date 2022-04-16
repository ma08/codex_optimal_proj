

letters = [0] * 26

for letter in input().lower():
    letters[ord(letter) - 97] += 1

print(sum(1 for letter in letters if letter % 2 != 0))
