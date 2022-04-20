
def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))

    temperature = [abs(t - h[i] * 0.006 - a) for i in range(n)]
    print(temperature.index(min(temperature)) + 1)


if __name__ == "__main__":
    main()
