

n = int(input())
change = 1000 - n % 1000
print(change if change < 1000 else 0)
