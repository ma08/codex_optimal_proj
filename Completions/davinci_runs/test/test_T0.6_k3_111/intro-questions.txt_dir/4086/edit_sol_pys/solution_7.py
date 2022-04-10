
def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                a[j] = 0
    b = list(set(a))
    b.sort(reverse=True)
    print(len(b))
    print(' '.join(map(str, b)))


if __name__ == '__main__':
    main()
