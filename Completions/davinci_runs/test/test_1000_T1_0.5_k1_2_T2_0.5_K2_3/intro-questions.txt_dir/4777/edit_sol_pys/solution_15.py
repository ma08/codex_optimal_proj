import sys

def fibonacci(k):
    x, y = 1, 0
    for _ in range(k):
        x, y = y, x + y
    return x, y

if __name__ == "__main__":
    k = int(sys.stdin.readline())
    x, y = fibonacci(k)
    print(x, y)
