

s = input()

if int(s[2:]) >= 1 and int(s[2:]) <= 12 and int(s[:2]) >= 1 and int(s[:2]) <= 12:
        print('AMBIGUOUS')
else:
    if int(s[2:]) >= 1 and int(s[2:]) <= 12:
        print('MMYY')
    elif int(s[:2]) >= 1 and int(s[:2]) <= 12:
        print('YYMM')
    else:
        print('NA')
