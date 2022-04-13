
def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    c = list(map(int, input().split(' ')))
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if a[i] == b[j]:
                for k in range(j, n):
                    if b[j] == c[k]:
                        cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
