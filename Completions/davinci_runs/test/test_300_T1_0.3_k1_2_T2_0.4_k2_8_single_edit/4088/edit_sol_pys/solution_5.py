

def get_b(s):
    b = []
    for i in range(len(s)):
        b.append(sum([abs(i-j) for j in range(len(s)) if s[j] > s[i]]))
    return b

def get_s(b):
    s = ''
    for i in range(len(b)):
        s += chr(ord('a')+i)
    return s

def get_t(s, b):
    t = ''
    for i in range(len(b)):
        t += s[b[i]]
    return t


for _ in range(int(input())):
    s = input()
    m = int(input())
    b = [int(i) for i in input().split()]
    print(get_t(get_s(b), b))
