

N = int(input())
change = 1000 - N % 1000
print(change if change != 1000 else 0)
