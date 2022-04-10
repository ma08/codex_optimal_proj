
n = input()

if n[-2:] == '00':
    print 0
elif n[-2:] in ['25', '50', '75']:
    print 1
elif n[-1] in ['0', '5']:
    print 2
else:
    print -1
