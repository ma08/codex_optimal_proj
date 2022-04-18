
s = input() 

if int(s[2:]) >= 1 and int(s[2:]) <= 12:
    if int(s[:2]) >= 1 and int(s[:2]) <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if int(s[:2]) >= 1 and int(s[:2]) <= 12:
        print('YYMM')
    else:
        print('NA')
