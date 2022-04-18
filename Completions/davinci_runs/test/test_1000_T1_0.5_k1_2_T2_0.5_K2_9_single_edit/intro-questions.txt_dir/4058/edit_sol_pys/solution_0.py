

def get_input():
    n, m = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    return n, m, a

def solve(n, m, a):
    k = [0] * n
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                k[i] += 1
    k.sort()
    k.reverse()
    for i in range(n):
        if k[i] < i + 1:
            return i
    return n

def main():
    n, m, a = get_input()
    ans = solve(n, m, a)
    print(ans)

if __name__ == '__main__':
    main()
