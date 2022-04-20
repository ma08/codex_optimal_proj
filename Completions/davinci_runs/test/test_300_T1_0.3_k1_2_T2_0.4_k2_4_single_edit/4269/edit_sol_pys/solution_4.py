

s = input()  # input()で入力を受け付ける

if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:  # 条件に合うか判定する
    print("Bad")  # 条件に合う場合
else:
    print("Good")  # 条件に合わない場合
