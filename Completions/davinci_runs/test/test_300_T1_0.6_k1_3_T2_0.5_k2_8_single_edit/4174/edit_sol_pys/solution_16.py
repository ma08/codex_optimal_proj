

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    s = 0
    if s <= x:
        cnt += 1
    cnt = 0
    for i in range(n):
        s += l[i]
        if s <= x and d == 0:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
