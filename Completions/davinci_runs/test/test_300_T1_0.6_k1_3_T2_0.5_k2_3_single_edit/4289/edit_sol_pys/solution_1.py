

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))

    temp = [abs(t - h[i] * 0.006 - a) for i in range(n)]
    print(temp.index(min(temp)) + 1)


if __name__ == "__main__":
    main()
