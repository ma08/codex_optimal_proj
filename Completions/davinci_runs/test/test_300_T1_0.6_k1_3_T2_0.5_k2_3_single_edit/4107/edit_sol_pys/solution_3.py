

def solve(l, r, k):
    if l == r:
        return l
    else:
        return k

if __name__ == '__main__':
    l, r, k = map(int, input().split())
    print(solve(l, r, k))
