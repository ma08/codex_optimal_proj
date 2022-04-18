

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        if n >= a[i]:
            n -= a[i]
            count += 1
        else:
            break
    print(count)

main()
