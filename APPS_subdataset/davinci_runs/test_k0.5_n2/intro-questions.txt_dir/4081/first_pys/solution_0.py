

def read_array():
    return [int(i) for i in input().split()]

def read_single_int():
    return int(input())

def solve(a):
    n = len(a)
    l = [0] * n
    r = [0] * n

    for i in range(1, n):
        if a[i] > a[i - 1]:
            l[i] = l[i - 1] + 1
        else:
            l[i] = 0

    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:
            r[i] = r[i + 1] + 1
        else:
            r[i] = 0

    ans = 0
    sol = []

    for i in range(n):
        if l[i] + r[i] + 1 > ans:
            ans = l[i] + r[i] + 1
            sol = [1] * (l[i] + 1)
            sol += [0] * (r[i] + 1)

    return ans, sol

def main():
    n = read_single_int()
    a = read_array()
    ans, sol = solve(a)
    print(ans)
    print("".join("L" if i else "R" for i in sol))

if __name__ == '__main__':
    main()