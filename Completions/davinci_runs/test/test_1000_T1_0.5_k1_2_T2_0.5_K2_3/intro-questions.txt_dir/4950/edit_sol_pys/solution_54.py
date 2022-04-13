
def main():
    """
    input:
        n: number of photographs
        t: time in hours
        d: distance in miles
    output:
        max speed in mph
    """
    n = int(input())
    speeds = []
    for _ in range(n):
        t, d = map(int, input().split())
        speeds.append(d / t)
    print(int(max(speeds)), end="")

if __name__ == "__main__":
    main()
