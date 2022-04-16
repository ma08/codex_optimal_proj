

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
    max_speed = 0
    for _ in range(n):
        t, d = map(int, input().split())
        speed = d / t
        if speed > max_speed:
            max_speed = speed
    print(int(max_speed))

if __name__ == "__main__":
    main()
