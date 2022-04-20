

    # n, k = map(int, input().split())
    # a = [0] * n
    # for i in range(k):
    #     d = int(input())
    #     b = list(map(int, input().split()))
    #     for j in range(d):
    #         a[b[j] - 1] += 1
    # print(a.count(0))

def main():
    n, k = map(int, input().split())
    a = [0] * (n + 1)
    for i in range(k):
        d = int(input())
        a[d] += 1
    print(a.count(0) - 1)

if __name__ == '__main__':
    main()
