

def double_ee(s):
    if (s[0] == 'h') and (s[1] == 'e') and (s[-1] == 'y') and (len(s) > 2):
        return s[0] + s[1] + s[1] + s[-1]
    else:
        return 'Invalid Input'

print(double_ee(input()))
