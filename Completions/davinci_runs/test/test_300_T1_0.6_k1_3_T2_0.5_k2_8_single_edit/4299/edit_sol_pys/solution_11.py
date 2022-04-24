
n = int(input())

if int(n[-1]) == 2 or int(n[-1]) == 4 or int(n[-1]) == 5 or int(n[-1]) == 7 or int(n[-1]) == 9:
    print("hon")
elif int(n[-1]) == 0 or int(n[-1]) == 1 or int(n[-1]) == 6 or int(n[-1]) == 8:
    print("pon")
elif int(n[-1]) == 3:

# 模範解答
n = int(input())

if n % 10 in [2, 4, 5, 7, 9]:
    print('hon')
elif n % 10 in [0, 1, 6, 8]:
    print('pon')
else:
    print('bon')
    print("bon")
