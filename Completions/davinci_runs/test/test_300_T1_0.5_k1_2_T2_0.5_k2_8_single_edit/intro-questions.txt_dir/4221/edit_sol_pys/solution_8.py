
# -*- coding: utf-8 -*-
s = input()
if s[-1] == "s":
    print(s + "es")
elif s[-1] == "h" and (s[-2] == "c" or s[-2] == "s"):
    print(s + "es")
elif s[-1] == "f":
    print(s[0:-1] + "ves")
elif s[-2:] == "fe":
    print(s[0:-2] + "ves")
elif s[-1] == "y":
    print(s[0:-1] + "ies")
else: print(s + "s")
