
def main():
    n, k = map(int, input().split())
    if k == 0:
        print(1)
    elif k == 1:
        print(n)
    else:
        if n == 1 and k == 1:
            print(1)
        else:
            if n < k:
                print(0)
            elif n > k:
                a = [1]
                for i in range(k - 1):
                    a.append(2 * a[i])
                if sum(a) == n:
                    print(a[k-1])
                else:
                    print(0)
            else:
                print(0)

if __name__ == "__main__":
    main()
