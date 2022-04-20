

def main():
    n, k = map(int, input().split())
    l = sorted(map(int, input().split()))
    if k == 0:
        print(1)
        return
    if k == n:
        print(l[-1])
        return
    if l[k-1] == l[k]:
        print(-1)
        return
    print(l[k-1])

if __name__ == '__main__':
    main()
