

s = input()
a = s[:int((len(s)-1)/2)]
b = s[int((len(s)+3)/2)-1:]
print("Yes" if s == s[::-1] and a == a[::-1] and b == b[::-1] else "No")
