

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            print("even")
        else:
            print("odd")

if __name__ == "__main__":
    main()
