

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if arr[i] + arr[j] == m:
                print(str(i + 1) + " " + str(j + 1))
                exit()
    print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
