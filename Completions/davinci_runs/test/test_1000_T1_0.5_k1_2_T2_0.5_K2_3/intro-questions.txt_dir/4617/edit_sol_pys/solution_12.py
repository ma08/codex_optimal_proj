
s = input()
c1 = s[0:len(s)//2]
c2 = s[len(s)//2:]

if c1[::-1] == c2:
    print("yes")
else:
    print("no")
