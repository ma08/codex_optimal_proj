

x = int(input())
i = 0
while True:
    i += 1
    x = int(x * 1.01)
    if x >= 1000000000000000000:
        break
print(i)