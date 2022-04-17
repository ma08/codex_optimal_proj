
n = int(input())
num = [int(i) for i in input().split()]  # список из чисел

for i in num:
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:  # если число делится на 2 и не делится на 3 и 5
        print("DENIED")
        exit()  # завершает программу

print("APPROVED")
