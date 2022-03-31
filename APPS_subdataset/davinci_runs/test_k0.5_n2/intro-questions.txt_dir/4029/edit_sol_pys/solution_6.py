

n = int(input())

if n % 100 == 0:
    print 0
elif n % 25 == 0: 
    print 1
elif n[-1] in ['0', '5']:
    print 2
else:
    print -1
