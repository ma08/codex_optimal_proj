

#input
s = input()

#output
for i in range(5):
    for j in range(len(s)):
        if i == 0 or i == 4:
            if j%3 == 2:
                print('.'*4, end='')
            else:
                print('.'*2, end='')
            if j != len(s)-1:
                print('#', end='')
        elif i == 1 or i == 3:
            if j%3 == 2:
                print('.'*3, end='')
            else:
                print('.', end='')
            if j != len(s)-1:
                print('#', end='')
        elif i == 2:
            if j%3 == 2:
                print('.'*2, end='')
            else:
                print('#', end='')
            if j != len(s)-1:
                print('.', end='')
        else:
            print(s[j], end='')
            if j != len(s)-1:
                print('#', end='')
            else:
                print('.'*2, end='')
    print()
