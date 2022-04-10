

def is_valid(n,m,s,d,c): #判断是否有解
    for i in range(m):
        if s[i] < d[i] - c[i]:
            return False
    return True


def solve(n,m,s,d,c): #解题
    if not is_valid(n,m,s,d,c):
        return -1
    res = [0]*n
    for i in range(m):
        for j in range(s[i] - 1,d[i]):
            res[j] = i + 1
        res[d[i] - 1] = m + 1
    return res

def main():
    n,m = map(int,input().split())
    s = []
    d = []
    c = []
    for i in range(m):
        si,di,ci = map(int,input().split())
        s.append(si)
        d.append(di)
        c.append(ci)
    res = solve(n,m,s,d,c)
    if res == -1:
        print(-1)
    else:
        for i in range(n):
            if i == n - 1:
                print(res[i])
            else:
                print(res[i],end=' ')

if __name__ == '__main__':
    main()
