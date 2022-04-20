

n = int(input())

if n % 10 in [0, 1, 6, 8]:
    print("pon\n")
elif n % 10 in [2, 4, 5, 7, 9]:
    print("hon\n")
elif n % 10 == 3:
    print("bon\n")
