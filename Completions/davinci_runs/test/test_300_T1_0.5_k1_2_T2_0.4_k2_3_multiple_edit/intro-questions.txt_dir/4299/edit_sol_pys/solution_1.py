
n = int(input())
one_place = n % 10

if one_place == 2 or one_place == 4 or one_place == 5 or one_place == 7 or one_place == 9:
    print("hon")
elif one_place == 0 or one_place == 1 or one_place == 6 or one_place == 8:
    print("pon")
elif one_place == 3:
    print("bon") 
