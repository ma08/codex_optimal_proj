
# Solution

s = input()

if len(s) > 1:
    if s.find('ss') == -1:
        print('no hiss')
    else: print('hiss')
else:
    print('no hiss')
