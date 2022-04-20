# AtCoder Beginner Contest 051
# Problem B - Sums of Sums
s = str(input())

if s[0] == 'A' and s[2:-1].count('C') == 1: # Aを含み、Cが1つしか含まれないとき
    for i in range(2, len(s)-1): # C以外の大文字
        if s[i] == 'C': # Cを除く
            continue 
        elif s[i].islower(): # 小文字を除く
            continue 
        else: # それ以外はWA
            print('WA') # WAを出力して終了
            exit() 
    print('AC') # ACを出力
else:
    print('WA')
