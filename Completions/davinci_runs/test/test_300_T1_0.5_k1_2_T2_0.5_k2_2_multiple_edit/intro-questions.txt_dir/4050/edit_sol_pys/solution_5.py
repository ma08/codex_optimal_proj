# https://codeforces.com/problemset/problem/1259/C

def find_max(a, n):
    for i in range(n-1, -1, -1):
        if a[i] == n-i:
            return i

def find_min(a, n):
    for i in range(n):
        if a[i] == i+1:
            return i

def main():
    n = int(input())
    a = [int(s) for s in input().split()][::-1]
    m = find_max(a, n)
    a = a[::-1]
    m = n-m-1
    res = []
    while True:
        m = find_min(a, n)
        if m == 0:
            break
        res.append(m)
        a = a[m:] + a[:m]
    print(len(res))
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    main()
