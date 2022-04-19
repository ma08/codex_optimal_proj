

n = int(input())
s = input()

if len(s) > n:
    print(s[:n] + '...')
else:
    print(s)
