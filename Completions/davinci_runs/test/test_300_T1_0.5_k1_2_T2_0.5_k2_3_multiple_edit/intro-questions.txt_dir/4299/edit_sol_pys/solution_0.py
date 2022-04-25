# coding: utf-8

n = input()

if n[-1] in ["0", "1", "6", "8"]:
    print("pon")
elif n[-1] in ["2", "4", "5", "7", "9"]:
    print("hon")
elif n[-1] == "3":
    print("bon")
