

def min_length(n, s):
    if n == 0:
        return 0
    else:
        return 1 + min_length(n-1, s[1:])

n = int(input())
s = input()

print(min_length(n, s))
