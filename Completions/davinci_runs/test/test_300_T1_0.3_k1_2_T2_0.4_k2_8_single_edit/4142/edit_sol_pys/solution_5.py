
s = input()

if all(c in "RUD" for c in s[::2]) and all(c in "LUD" for c in s[1::2]): # 偶数番目がRUD, 奇数番目がLUD
    print("Yes")
else:
    print("No")
