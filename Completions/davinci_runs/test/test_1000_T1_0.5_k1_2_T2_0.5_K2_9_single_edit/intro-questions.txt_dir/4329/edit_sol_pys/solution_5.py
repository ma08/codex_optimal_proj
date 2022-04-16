
s = input()
t = input()

if t[0:len(s)] == s:  # tの0文字目からsの文字数分の文字列とsが一致するか
    print('Yes')
else:
    print('No')
