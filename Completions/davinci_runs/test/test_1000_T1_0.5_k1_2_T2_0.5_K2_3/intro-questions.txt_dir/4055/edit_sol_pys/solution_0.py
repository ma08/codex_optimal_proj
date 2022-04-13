

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 1
    for i in range(1, n - 1):
        if a[i - 1] == 0 and a[i + 1] == 0 and a[i] == 1:
            a[i + 1] = 1
            count += 1
    print(count)

if __name__ == "__main__":
    main()
