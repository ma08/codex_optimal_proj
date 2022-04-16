

def main():
    n = int(input())
    x = int(input())
    a = [0] * n
    a[x - 1] = 1
    for i in range(n - 1):
        a[int(input()) - 1] += 1
    print(a.count(0))

if __name__ == "__main__":
    main()
