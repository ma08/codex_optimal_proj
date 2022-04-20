

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            num = int(str(a[i]) + str(a[j])
            if num % k == 0:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
