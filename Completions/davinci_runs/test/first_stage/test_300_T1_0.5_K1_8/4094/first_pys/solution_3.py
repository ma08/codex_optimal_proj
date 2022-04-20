

k = int(input())

for i in range(1, 10**6):
    if (int(str(7)*i) % k) == 0:
        print(i)
        exit()
print(-1)