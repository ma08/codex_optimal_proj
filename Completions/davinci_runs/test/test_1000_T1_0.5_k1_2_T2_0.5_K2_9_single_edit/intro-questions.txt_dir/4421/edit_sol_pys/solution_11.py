
s = input()
length = len(s)
if length % 2 == 0:
    print(s[:length//2-1] + s[length//2+1:])
else:
    print(s[:length//2] + s[length//2+1:])
