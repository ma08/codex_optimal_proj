

def main():
    n = int(input())
    speeds = []
    for _ in range(n):
        t, d = map(int, input().split())
        speeds.append(d / t)
    print(int(max(speeds)))

if __name__ == "__main__":
    main()
