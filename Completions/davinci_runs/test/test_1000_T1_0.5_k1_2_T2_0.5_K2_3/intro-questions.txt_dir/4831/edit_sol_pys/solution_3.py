

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
            if j % 3 == 2:
                print('.'*4, end='')
            else:
                print('.'*2, end='')
            if j != len(s)-1:
                print('#', end='')
        elif i == 1 or i == 3:
            if j % 3 == 2:
                print('.'*3, end='')
            else:
                print('.', end='')
            if j != len(s)-1:
                print('#', end='')
        elif i == 2:
            if j % 3 == 2:
                print('.'*2, end='')
            else:
                print('#', end='')
            if j != len(s)-1:
                print('.', end='')
            print(s[j], end='')#文字列
            if j != len(s)-1:
                print('#', end='')
            else:
                print('.'*2, end='')
    print()
