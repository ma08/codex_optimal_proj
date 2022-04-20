

def main():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        arr = [m//n]*n
        if m % n != 0:
            arr[-1] += 1
        print(max(arr) - min(arr))


if __name__ == "__main__":
    main()
