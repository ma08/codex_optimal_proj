
s = input()  # input: "abcde"
t = input()  # input: "cdeab"

if s == t: print('Yes')
elif len(s) == len(t):
    for i in range(len(s)):
        if s == t:
            print('Yes')
            break
        else:
            s = s[-1] + s[:-1]
    else: print('No')
else: print('No')
