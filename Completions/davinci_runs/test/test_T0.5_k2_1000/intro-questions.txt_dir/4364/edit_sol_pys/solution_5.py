

s = input()

if int(s[2:]) >= 1 and int(s[2:]) <= 12:  # if the last two digits are between 1 and 12
    if int(s[:2]) >= 1 and int(s[:2]) <= 12:  # if the first two digits are between 1 and 12
        print('AMBIGUOUS')
    else:
        print('MMYY')  # if the first two digits are not between 1 and 12
else:
    if int(s[:2]) >= 1 and int(s[:2]) <= 12:
        print('YYMM')
    else:
        print('NA')
