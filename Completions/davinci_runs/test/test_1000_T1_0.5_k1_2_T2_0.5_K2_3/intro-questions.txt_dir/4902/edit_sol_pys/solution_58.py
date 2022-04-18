#read input
from sys import stdin
#create a list of 26 elements
s = stdin.readline().strip().lower()
#loop through the string and add the number of times the letter appears in the string to the appropriate index in the list
letters = [0]*26
for c in s:
    letters[ord(c)-ord('a')] += 1
#count the number of letters that appear an odd number of times
num_odds = 0
for i in range(len(letters)):
    if letters[i] % 2 == 1:
        num_odds += 1
if num_odds > 1:
    print(num_odds-1)
else:
    print(0)
