

def double_e(s):
    if s[0] == 'h' and s[1] == 'e' and s[-1] == 'y':
        return s[0] + s[1] + s[1] + s[-1]
    else:
        return 'Invalid Input'

print(double_e(input()))
