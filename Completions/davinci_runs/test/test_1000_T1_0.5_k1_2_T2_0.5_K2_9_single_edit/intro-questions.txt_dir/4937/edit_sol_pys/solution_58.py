
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)

if __name__ == "__main__":
    main()
