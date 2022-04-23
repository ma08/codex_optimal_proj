# coding: utf-8

n = int(input())
one_place = n % 10

if one_place == 2 or one_place == 4 or one_place == 5 or one_place == 7 or one_place == 9:
    print("hon")  # 末尾が2, 4, 5, 7, 9のとき
elif one_place == 0 or one_place == 1 or one_place == 6 or one_place == 8:
    print("pon")  # 末尾が0, 1, 6, 8のとき
elif one_place == 3:
    print("bon")
