

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(read_books(n, m, k, a, b))


def read_books(n, m, k, a, b):
    cnt = 0
    for i in range(k):
        if a[i] < b[i]:
            cnt += 1

    return cnt




if __name__ == '__main__':
    main()
