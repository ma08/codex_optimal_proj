
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/char-sum-2d3a6ab5/
#Solution

s = input()
n = len(s)
i = 0
while i < n:
    if s[i] == '<':
        i -= 1
        if i < 0:
            i = 0
        s = s[:i] + s[i+1:]
        n -= 1
        i -= 1
    else:
        i += 1
print(s)
