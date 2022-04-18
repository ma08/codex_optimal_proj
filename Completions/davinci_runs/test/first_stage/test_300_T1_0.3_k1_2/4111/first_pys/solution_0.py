

def main():
    n = int(input())
    a = list(map(int, input().split()))
    odd = 0
    even = 0
    count = 0
    for i in range(n):
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]
    for i in range(n):
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