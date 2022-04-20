

def main():
    n = int(input())
    a = list(map(int, input().split()))
    odd = a[0]
    even = a[1]
    count = 0
    for i in range(2, n):
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]
    for i in range(1, n):
        if i % 2 == 0:
            even -= a[i]
        else:
            odd -= a[i]
        if even == odd:
            count += 1
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]
    print(count)

if __name__ == "__main__":
    main()
