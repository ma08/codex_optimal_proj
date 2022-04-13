
# 
from sys import stdin

s = stdin.readline().strip()

letters = [0]*26

for c in s:
    letters[ord(c)-ord('a')] += 1

num_odds = 0
for i in range(len(letters)):
    if letters[i] % 2 == 1:
        num_odds += 1

if num_odds > 1:
    print(num_odds - 1)
else:
    print(0)
