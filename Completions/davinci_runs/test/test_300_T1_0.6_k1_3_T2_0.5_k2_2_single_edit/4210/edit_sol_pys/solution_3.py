

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            num = int(str(a[i]) + str(a[j])) % k
            count += 1 if num == 0 else 0
    print(count)

if __name__ == "__main__":
    main()
