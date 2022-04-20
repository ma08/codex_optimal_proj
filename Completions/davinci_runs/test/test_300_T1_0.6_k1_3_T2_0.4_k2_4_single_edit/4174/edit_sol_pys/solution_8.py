

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    s = 0
    cnt = 0
    for i in range(n):
        s += l[i]
        if s <= x:
            cnt += 1
    print(cnt + 1)

if __name__ == '__main__':
    main()
