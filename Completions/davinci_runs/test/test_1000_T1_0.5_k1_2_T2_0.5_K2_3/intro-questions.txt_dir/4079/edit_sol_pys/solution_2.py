
import string
# Solution 

n = int(input())

for i in range(n):
    s = input()
    print('Yes' if set(s) == set(string.ascii_lowercase[:len(s)]) else 'No')
