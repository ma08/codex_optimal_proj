

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                a[j] = 0
    a = list(set(a))
    a.sort(reverse=True)
    print(len(a))
    print(' '.join(map(str, a)))


if __name__ == '__main__':
    main()