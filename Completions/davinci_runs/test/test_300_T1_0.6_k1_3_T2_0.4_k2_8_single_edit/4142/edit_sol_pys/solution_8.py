

s = input()

if len(s) % 2 == 0:
    if s[0] == "R" or s[0] == "U" or s[0] == "D":  # 偶数の場合、最初がRかUかDの場合
        for i in range(1, len(s), 2):
            if s[i] != "L" and s[i] != "U" and s[i] != "D":
                print("No")
                break
        else:
            print("Yes")
    else:  # それ以外はNo
        print("No")
else:
    if s[0] == "L" or s[0] == "U" or s[0] == "D":  # 奇数の場合、最初がLかUかDの場合
        for i in range(1, len(s), 2):
            if s[i] != "R" and s[i] != "U" and s[i] != "D":
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
