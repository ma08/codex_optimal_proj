
def main():
    """
    Input:
        n: number of photographs
        t: time in hours
        d: distance in miles
    Output:
        max speed in mph
    """
    n = int(input())
    speeds = []
    for _ in range(n):
        t, d = map(int, input().split())
        speeds.append(d / t)
    print(int(max(speeds)))

if __name__ == "__main__":
    main()
