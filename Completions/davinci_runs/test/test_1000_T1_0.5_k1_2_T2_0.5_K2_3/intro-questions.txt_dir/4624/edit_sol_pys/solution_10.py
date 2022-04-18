
import math

def find_floor(n, x):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return int(math.ceil((n-2)/x)) + 2

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        print(find_floor(n, x))
