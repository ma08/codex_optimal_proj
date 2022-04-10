

def f(a, n, f):
    a = list(a)
    for i in range(n):
        a[i] = str(f[int(a[i])])
    return int("".join(a))

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    print(max(f(a, n, f), f(a[::-1], n, f[::-1])))

if __name__ == "__main__":
    main()