
s = input()

if int(s[2:]) >= 1 and int(s[2:]) <= 12: # if the last two digits are between 1 and 12
    if int(s[:2]) >= 1 and int(s[:2]) <= 12:
        print('AMBIGUOUS') # if the first two digits are between 1 and 12
    else:
        print('MMYY') # if the first two digits are not between 1 and 12
else:
    if int(s[:2]) >= 1 and int(s[:2]) <= 12:
        print('YYMM') # if the first two digits are between 1 and 12
    else:
        print('NA') # if the first two digits are not between 1 and 12
