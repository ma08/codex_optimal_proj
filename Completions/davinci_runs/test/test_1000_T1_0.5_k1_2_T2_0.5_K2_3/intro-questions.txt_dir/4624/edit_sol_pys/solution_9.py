
def find_floor(n, x):
    floor = 1
    n -= x
    if n <= 0:
        return floor
    while n > 0:
        n -= x
        floor += 1
    return floor

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        print(find_floor(n, x))
