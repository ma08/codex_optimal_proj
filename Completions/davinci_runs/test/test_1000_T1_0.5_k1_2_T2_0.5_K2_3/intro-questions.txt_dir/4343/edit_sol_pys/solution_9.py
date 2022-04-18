

def median_string(s, t):
    if s == t:
        return s
    
    mid = (ord(t[0]) - ord(s[0])) // 2
    if mid == 0:
        return s + median_string(s[1:], t[1:])
    if mid == ord(t[0]) - ord(s[0]):
        return t[0] + median_string(s[1:], t[1:])
    
    return chr(ord(s[0]) + mid) + median_string(s[1:], t[1:])

k = int(input())
s = input()
t = input()

print(median_string(s, t))
