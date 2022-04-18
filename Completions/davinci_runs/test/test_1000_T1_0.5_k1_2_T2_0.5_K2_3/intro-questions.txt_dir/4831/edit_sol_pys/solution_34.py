

#input
s = input()

#パターン
#1
#2
#3
#4
#5
#output
for i in range(5):
    for j in range(len(s)):
        if i == 0 or i == 4:
            if j%3 == 2:
                print('.'*4, end='')#4個の点
            else:
                print('.'*2, end='')#2個の点
            if j != len(s)-1:
                print('#', end='')#文字列の区切り
        elif i == 1 or i == 3:
            if j%3 == 2:
                print('.'*3, end='')#3個の点
            else:
                print('.', end='')#1個の点
            if j != len(s)-1:
                print('#', end='')#文字列の区切り
        elif i == 2:
            if j%3 == 2:
                print('.'*2, end='')#2個の点
            else:
                print('#', end='')#文字列の区切り
            if j != len(s)-1:
                print('.', end='')#文字列の区切り
            print(s[j], end='')#文字列
            if j != len(s)-1:
                print('#', end='')#文字列の区切り
            else:
                print('.'*2, end='')
    print()
