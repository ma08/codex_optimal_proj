# coding: utf-8

s = input()
t = input()

if s == t:
    print("Yes")
else:
    if len(s) == len(t):
        for i in range(len(s)):
            if s == t:
                print("Yes")
                break
            else:
                s = s[-1] + s[:-1] # 一文字目を末尾にした新しい文字列を作る
        else:
            print("No")
    else:
        print("No")
