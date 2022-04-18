
s = input()

if s == s[::-1]:
    if s[:(len(s)-1)//2] == s[:(len(s)-1)//2][::-1]: # 前半分を判定
        if s[(len(s)+3)//2-1:] == s[(len(s)+3)//2-1:][::-1]: # 後半分を判定
            print('Yes')
            exit()
print('No')
