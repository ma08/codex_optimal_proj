

n = int(input())

for i in range(n):
    x = int(input())
    if i == 0:
        low_num = 1
        high_num = x
    else:
        low_num = x + 1
        high_num = x

for i in range(low_num, high_num+1):
    print(i)
