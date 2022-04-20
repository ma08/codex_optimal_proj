

def main():
    n = int(input())
    a = list(map(int, input().split())
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print(a)

if __name__ == "__main__":
    main()
