
def main():
    n, k = map(int, input().split())
    if n >= k:
        a = [1]
        for i in range(1, k):
            if a[-1] * 2 - 1 < n:
                a.append(a[-1] * 2 - 1)
            else:
                a.append(n)
                break
        else:
            if a[-1] * 2 - 1 == n:
                a.append(n)
            else:
                print("NO")
                return
        a[-1] = n - sum(a[:-1])
        print("YES")
        print(*a)
    else:
        print('NO')

if __name__ == "__main__":
    main()
