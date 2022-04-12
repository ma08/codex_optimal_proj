N = int(input())

print("Yes" if N % sum([int(x) for x in list(str(N))]) == 0 else "No")
