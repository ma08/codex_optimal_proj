

def main():
    n, m = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]

    cnt = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if p[i:j][len(p[i:j])//2] == m:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()