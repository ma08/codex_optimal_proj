

s = input()  # 後ろから一文字ずつsに入れていく
t = input()  # 後ろから一文字ずつtに入れていく

if s == t:  # sとtが同じならYesを出力
    print("Yes")
else:  # sとtが違うなら
    if len(s) == len(t):  # sとtの長さが同じなら
        for i in range(len(s)):
            if s == t:  # sとtが同じならYesを出力
                print("Yes")
                break
            else:  # sとtが違うなら
                s = s[-1] + s[:-1]
        else:
            print("No")
    else:
        print("No")
