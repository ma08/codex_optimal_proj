

str = input()
for i in range(len(str)-1):
    if str[i] == 's' and str[i+1] == 's':
        print('hiss')
        break
else:
    print('no hiss')
