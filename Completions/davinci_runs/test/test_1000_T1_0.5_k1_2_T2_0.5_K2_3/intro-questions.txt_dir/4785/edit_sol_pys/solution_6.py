# This program will tell if the input string has a hiss or not
# Solution

s = input()

if len(s) > 1:
    for i in range(len(s) - 1):
        if s[i] == 's' and s[i + 1] == 's':
            print('hiss')
            break
    else:
        print('no hiss')
else:
    print('no hiss')
