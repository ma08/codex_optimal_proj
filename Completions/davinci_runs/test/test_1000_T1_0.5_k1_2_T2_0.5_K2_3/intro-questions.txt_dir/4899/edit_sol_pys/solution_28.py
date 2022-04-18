

def double_e(s):
    if s[0] == 'h' and s[1] == 'e' and s[-1] == 'y' and len(s) > 1:
        return s[0] + s[1] + s[1] + s[-1] + 'y'
    else:
        return 'Invalid Input. Please enter a valid word'


print(double_e(input("enter a word: ")))
