
# SOLUTION

def main():
    t = int(input())
    for i in range(t):
        a, b, x, y, n = map(int, input().split())
        if a - x > b - y:
            a -= min(n, a - x)
            n -= min(n, a - x)
            b -= min(n, b - y)
        else:
            b -= min(n, b - y)
            n -= min(n, b - y)
            a -= min(n, a - x)
        print(a * b)

if __name__ == "__main__":
    main()

# SOLUTION

def main():
    t = int(input())
    for i in range(t):
        a, b, x, y, n = map(int, input().split())
        if a - x > b - y:
            a -= min(n, a - x)
            n -= min(n, a - x)
            b -= min(n, b - y)
        else:
            b -= min(n, b - y)
            n -= min(n, b - y)
            a -= min(n, a - x)
        print(a * b)

if __name__ == "__main__":
    main()
