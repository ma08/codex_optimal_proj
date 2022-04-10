

# Solution

# python3

n = input()

if n.count('0') == len(n) - 1:
    print(-1)
else:
    n = n.lstrip('0')
    print(len(n) - 1)