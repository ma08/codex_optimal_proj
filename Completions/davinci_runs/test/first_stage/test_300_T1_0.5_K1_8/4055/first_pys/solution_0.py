

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(1, n-1):
        if a[i-1] == 1 and a[i+1] == 1 and a[i] == 0:
            c += 1
            a[i] = 1
    print(c)

if __name__ == "__main__":
    main()