

def median(s, t, k):
    if len(s) == len(t):
        return (s, t)
    
    mid = (ord(t[0]) - ord(s[0])) // 2 + 1
    if mid == 1:
        return (s[0] + median(s[1:], t[1:], k - 1)[0], s[0] + median(s[1:], t[1:], k - 1)[1])
    if mid == ord(t[0]) - ord(s[0]):
        return (t[0] + median(s[1:], t[1:], k - 1)[0], t[0] + median(s[1:], t[1:], k - 1)[1])
    
    return (chr(ord(s[0]) + mid) + median(s[1:], t[1:], k - 1)[0], chr(ord(s[0]) + mid) + median(s[1:], t[1:], k - 1)[1])

k = int(input())
s = input()
t = input()

print(median(s, t, k)[0])
print(median(s, t, k)[1])
