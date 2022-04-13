

n = int(input())
print("Yes" if n % sum([int(x) for x in list(str(n))]) == 0 else "No")
