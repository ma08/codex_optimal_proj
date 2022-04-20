

s = input()

if s[0:int((len(s)-1)/2)] == s[0:int((len(s)-1)/2)][::-1] and \
    s[int((len(s)+3)/2)-1:len(s)] == s[int((len(s)+3)/2)-1:len(s)][::-1] and \
    s == s[::-1]:
    print("Yes")
else:
    print("No")