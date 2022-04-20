

def main():
    n, k = map(int, input().split())
    if k == 0 or k == n:
        print(1) if k == 0 else print(l[-1])
    else:
        l = list(map(int, input().split()))
        l.sort()
        if l[k-1] == l[k]:
            print(-1)
        else:
            print(l[k-1])

if __name__ == '__main__':
    main()
