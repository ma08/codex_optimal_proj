


def get_permutation(n,a,b,c):
    p = []
    for i in range(n):
        p.append(a)
        p.append(b)
        p.append(c)
    return p

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        p = get_permutation(n)
        if p[0] == -1:
            print(-1)
        else:
            print(*p)

main()
