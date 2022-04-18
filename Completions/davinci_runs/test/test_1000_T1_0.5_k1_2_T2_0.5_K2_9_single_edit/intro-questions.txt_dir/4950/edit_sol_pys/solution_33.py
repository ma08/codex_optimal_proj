

def main():
    """
    input:
        n: number of photographs
        t: time in hours
        d: distance in miles
    output:
        max speed in mph
    """
    n = int(input()) # number of photographs
    speeds = []
    for _ in range(n):
        t, d = map(int, input().split()) # time in hours, distance in miles
        speeds.append(d / t)
    print(int(max(speeds)))

if __name__ == "__main__":
    main()
