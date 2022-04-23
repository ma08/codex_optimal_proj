

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    l = []
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            l.append(a[i])
    if len(l) > 0:
        print(len(l))
        print(' '.join([str(i) for i in l]))
    else:
        print(0)

if __name__ == '__main__':
    main()
