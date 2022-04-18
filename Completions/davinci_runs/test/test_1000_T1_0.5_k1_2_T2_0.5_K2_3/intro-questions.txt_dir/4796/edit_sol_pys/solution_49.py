

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        count += a[i]
    for i in range(k):
        if a[i] < 0:
            count -= a[i]
    print(count)

main()
