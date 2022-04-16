
def find_floor(n, x):
    if n <= 1:
        return 1
    return 1 + ((n - 2) // x)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        print(find_floor(n, x))
