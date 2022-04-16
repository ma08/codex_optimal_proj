
q = int(input())
for i in range(1, q+1):
    a = int(input())
    if a == 1:
        print(str(2))
    elif a == 2:
        print(str(3))
    else:
        sum = 1
        for j in range(1, a+1):
            sum = sum + j
        print(str(sum))
