

def mediana(s, t, k):
    if s == t:
        return s
    
    mid = (ord(t[k]) - ord(s[k])) // 2
    if mid == 0:
        return s[k] + mediana(s[1:], t[1:], k + 1)
    if mid == ord(t[k]) - ord(s[k]):
        return t[k] + mediana(s[1:], t[1:], k + 1)
    
    return chr(ord(s[k]) + mid) + mediana(s[1:], t[1:], k + 1)

k = int(input())
s = input()
t = input()

print(mediana(s, t, 0))
