

def main():
    n, k = map(int, input().split())
    if n < k:
        print("NO")
        return
    a = []
    for i in range(1, k):
        if len(a) == 0 or a[-1] * 2 - 1 < n:
            a.append(1)
        else:
            a.append(n)
            break
    else:
        if len(a) == 0 or a[-1] * 2 - 1 == n:
            a.append(n)
        else:
            print("NO")
            return
    a[-1] = n - sum(a[:-1])
    print("YES")
    print(*a)

if __name__ == "__main__":
    main()
