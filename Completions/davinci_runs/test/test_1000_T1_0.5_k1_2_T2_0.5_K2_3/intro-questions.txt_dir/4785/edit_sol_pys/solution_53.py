

# Solution 1 - Run time O(n)

def hiss(s):
    if len(s) > 1:
        for i in range(len(s)-1):
            if s[i] == 's' and s[i+1] == 's':
                print('hiss')
                break
        else:
            print('no hiss')
    else:
        print('no hiss')

hiss('hissssssssss')
