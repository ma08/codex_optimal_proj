

N = int(input())
change = 1000 - N % 1000 if N % 1000 != 0 else 0
print(change)
