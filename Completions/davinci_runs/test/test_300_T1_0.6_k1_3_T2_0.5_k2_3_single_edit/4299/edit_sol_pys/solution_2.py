

n = input().split()

for i in n:
    if int(i[-1]) == 2 or int(i[-1]) == 4 or int(i[-1]) == 5 or int(i[-1]) == 7 or int(i[-1]) == 9:
        print("hon")
    elif int(i[-1]) == 0 or int(i[-1]) == 1 or int(i[-1]) == 6 or int(i[-1]) == 8:
        print("pon")
    elif int(i[-1]) == 3:
        print("bon")
