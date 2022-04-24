

n = int(input())
num = [int(i) for i in input().split()]

if n == 1:
    if num[0] % 2 == 0 and num[0] % 3 != 0 and num[0] % 5 != 0:
        print("DENIED")
    else:
        print("APPROVED")
else:
    for i in num:
        if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
            print("DENIED")
            exit()

    print("APPROVED")
