

from collections import Counter

n = int(input())
s = input()

# count the number of each character
# if there are more than 2 characters, the answer is 2
# if there are 2 characters, the answer is 1
# if there is 1 character, the answer is 1
# in any case, the answer is the number of distinct characters

c = Counter(s)

if len(c) == 1:
    print(1)
    print(' '.join([str(1)] * n))
elif len(c) == 2:
    print(1)
    for i in range(n):
        if c[s[i]] == 1:
            print(2, end=' ')
        else:
            print(1, end=' ')
    print()
else:
    print(2)
    for i in range(n):
        if c[s[i]] == 1:
            print(2, end=' ')
        else:
            print(1, end=' ')
    print()