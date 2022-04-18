

k = int(input())
s = str(input())

print(s[0:k] + "..." if k < len(s) else s)
