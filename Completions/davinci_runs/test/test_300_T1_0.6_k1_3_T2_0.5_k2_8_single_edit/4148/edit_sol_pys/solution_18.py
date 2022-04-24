

n = int(input())
s = input().split()
s = s[:n] + s[n + 1:]
print(' '.join(s))
