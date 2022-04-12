

def mediana(s, t):
    if s == t:
        return s
    
    mid = (ord(t[0]) - ord(s[0])) // 2 + 1
    if mid == 0:
        return s + mediana(s[1:], t[1:])
    if mid == ord(t[0]) - ord(s[0]):
        return t + mediana(s[1:], t[1:])
    
    return chr(ord(s[0]) + mid) + mediana(s[1:], t[1:])

k = int(input())
s = input()
t = input()

print(mediana(s, t))
