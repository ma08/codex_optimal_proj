

def main():
    n, k = map(int, input().split())
    a = [0] * n
    for i in range(k):
        d = int(input())
        a_i = list(map(int, input().split()))
        for j in range(d):
            a[a_i[j] - 1] += 1
    print(a.count(0))

if __name__ == "__main__":
    main()
