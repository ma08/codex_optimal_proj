

# -----Answer-----
s = input() # 入力された文字列をsに代入

if s[0] == 'A' and s[1].islower() and s[2].islower() and s[3] == 'C' and s[4:].islower(): # 条件分岐
    print("AC")
else:
    print("WA")

# -----Answer-----
# s = input() # 入力された文字列をsに代入
#
# if s[0] == 'A' and s[1].islower() and s[2].islower() and s[3] == 'C' and s[4:].islower(): # 条件分岐
#     print("AC")
# else:
#     print("WA")
