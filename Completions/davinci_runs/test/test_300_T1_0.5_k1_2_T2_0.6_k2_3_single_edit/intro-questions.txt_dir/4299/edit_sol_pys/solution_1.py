

n = int(input())
one_place = n % 10

if one_place in [2, 4, 5, 7, 9]:
    print("hon")
elif one_place in [0, 1, 6, 8]:
    print("pon")
elif one_place == 3:
    print("bon")
