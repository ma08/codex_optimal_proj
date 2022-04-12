

def mediana(s, t, l):
    if l == 0:
        return ''
    mid = (ord(t[0]) - ord(s[0])) // 2 + ord(s[0])
    if mid == ord(s[0]):
        return s[0] + mediana(s[1:], t[1:], l - 1)
    if mid == ord(t[0]):
        return t[0] + mediana(s[1:], t[1:], l - 1)
    return chr(mid) + mediana(s[1:], t[1:], l - 1)

k = int(input())
s = input()
t = input()
print(mediana(s, t, k))
