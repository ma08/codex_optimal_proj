

n,m = map(int,input().split())

def check(num):
    num = str(num)
    for i in range(m):
        if num[s[i]-1] != str(c[i]):
            return False
    return True

s = []
c = []
for _ in range(m):
    si,ci = map(int,input().split())
    s.append(si)
    c.append(ci)

for i in range(n**10):
    if check(i):
        print(i)
        exit()
print(-1)