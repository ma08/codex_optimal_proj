

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    result = 2
    for i in range(1, n):
        if a[i-1] + 1 == a[i]:
            result += 1
    print(result)

if __name__ == "__main__":
    main()