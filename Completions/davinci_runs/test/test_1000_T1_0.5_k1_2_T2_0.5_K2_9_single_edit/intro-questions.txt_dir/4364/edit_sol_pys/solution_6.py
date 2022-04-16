
# coding: utf-8
s = input()

if int(s[2:]) >= 1 and int(s[2:]) <= 12:  # 2文字目以降が1から12までの数字の場合
    if int(s[:2]) >= 1 and int(s[:2]) <= 12:  # 1文字目から2文字目までが1から12までの数字の場合
        print('AMBIGUOUS')
    else:  # 1文字目から2文字目までが1から12までの数字でない場合
        print('MMYY')
else:  # 2文字目以降が1から12までの数字でない場合
    if int(s[:2]) >= 1 and int(s[:2]) <= 12:  # 1文字目から2文字目までが1から12までの数字の場合
        print('YYMM')
    else:  # 1文字目から2文字目までが1から12までの数字でない場合
        print('NA')
