

#input
s = input()

#output
for i in range(5):
    for j in range(len(s)):
        if i == 0 or i == 4:
            if j%3 == 2:
                print('.'*4, end='') #print 4 dots
            else:
                print('.'*2, end='') #print 2 dots
            if j != len(s)-1:
                print('#', end='') #print #
        elif i == 1 or i == 3:
            if j%3 == 2:
                print('.'*3, end='') #print 3 dots
            else:
                print('.', end='') #print 1 dot
            if j != len(s)-1:
                print('#', end='') #print #
        elif i == 2:
            if j%3 == 2:
                print('.'*2, end='') #print 2 dots
            else:
                print('#', end='') #print #
            if j != len(s)-1:
                print('.', end='') #print 1 dot
            print(s[j], end='') #print the character
            if j != len(s)-1:
                print('#', end='') #print #
            else:
                print('.'*2, end='') #print 2 dots
    print()
