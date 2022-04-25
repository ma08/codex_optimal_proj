

s = input()  # 入力

if s[0] == 'A' and s[2:-1].count('C') == 1:  # 先頭のAとCの数
    for i in range(2, len(s)-1):  # A以外の大文字の数
        if s[i] == 'C':  # Cは大文字でも小文字でも許可
            continue
        elif s[i].islower():  # 小文字は許可
            continue
        else:
            print('WA')  # それ以外はWA
            exit()
    print('AC')  # すべてOKならAC
else:
    print('WA')  # それ以外はWA
