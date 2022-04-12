

x = int(input())

time = 0
for i in range(10**9):
    if i * (i + 1) // 2 >= x:
        time = i
        break

print(time)
