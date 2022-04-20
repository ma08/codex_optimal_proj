

def main():
    n, k = map(int, input().split())
    if n < k:
        print("NO")
        return
    if k == 1:
        if n == 1:
            print("YES")
            print(1)
        else:
            print("NO")
    else: 
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

if __name__ == "__main__":
    main()
