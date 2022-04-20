

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    i = j = 0
    while i < n and j < m:
        if a[i] + k < b[j]:
            i += 1
        elif a[i] - k > b[j]:
            j += 1
        else:
            print(a[i], b[j])
            i += 1
            j += 1

if __name__ == '__main__':
    main()
