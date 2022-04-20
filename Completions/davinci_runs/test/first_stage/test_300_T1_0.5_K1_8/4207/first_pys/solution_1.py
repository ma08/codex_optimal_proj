

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    count = 0
    for i in range(n):
        if a[i] < 0 and b[i] > 0:
            count += 1
    if count > n//2:
        print(n - count)
    else:
        print(count)

if __name__ == "__main__":
    main()