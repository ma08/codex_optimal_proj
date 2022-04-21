

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if (a[i-1] == 1 and a[i+1] == 1 and a[i] == 0):
            count += 1nb
    print(count)

if __name__ == "__main__":
    main()
