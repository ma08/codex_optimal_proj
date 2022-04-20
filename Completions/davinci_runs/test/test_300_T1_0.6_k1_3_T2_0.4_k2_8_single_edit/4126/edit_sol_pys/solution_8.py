
s = input()

if s == s[::-1]:
    if s[:(len(s)-1)//2] == s[:(len(s)-1)//2][::-1]:
        if s[(len(s)+3)//2-1:] == s[(len(s)+3)//2-1:][::-1]: # 中央値が奇数個の場合
            print('Yes')
            exit()
print('No')
