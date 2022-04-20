

def main():
    """
    TLE
    """
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if a[j] > 2 * a[i]:
                break
            for k in range(j, n):
                if a[k] > 2 * a[j]:
                    break
                for l in range(k, n):
                    if a[l] > 2 * a[k]:
                        break
                    for m in range(l, n):
                        if a[m] > 2 * a[l]:
                            break
                        cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()