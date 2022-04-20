

def get_t(s, b):
    t = ''
    for i in range(len(b)):
        t += s[b[i]]
    return t

for _ in range(int(input())):
    s = input()
    m = int(input())
    b = [int(i) for i in input().split()]
    print(get_t(s, b))
