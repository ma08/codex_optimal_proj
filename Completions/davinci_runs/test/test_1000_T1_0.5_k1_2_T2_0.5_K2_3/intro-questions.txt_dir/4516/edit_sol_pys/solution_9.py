

"""
My solution:

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))

    for i in range(n):
        f = 0
        for j in range(m - 1):
            f += abs(x[j] - x[j + 1])
        print(f, end=' ')


if __name__ == "__main__":
    main()
"""

"""
Fastest solution:

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        s = 0
        for j in range(m - 1):
            if a[j] > i + 1 and a[j + 1] < i + 1:
                s += abs(a[j] - i - 1) + abs(a[j + 1] - i - 1)
            elif a[j] < i + 1 and a[j + 1] > i + 1:
                s += abs(a[j] - i - 1) + abs(a[j + 1] - i - 1)
            else:
                s += abs(a[j] - a[j + 1])
        print(s, end=" ")


if __name__ == "__main__":
    main()
"""

"""
# Another solution:

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    for i in range(1, n + 1):
        s = 0
        for j in range(m - 1):
            if x[j] > i and x[j + 1] < i:
                s += abs(x[j] - i) + abs(x[j + 1] - i)
            elif x[j] < i and x[j + 1] > i:
                s += abs(x[j] - i) + abs(x[j + 1] - i)
            else:
                s += abs(x[j] - x[j + 1])
        print(s, end=" ")


if __name__ == "__main__":
    main()
"""

"""
# One more solution:

n, m = map(int, input().split())
x = list(map(int, input().split()))
for i in range(1, n + 1):
    s = 0
    for j in range(m - 1):
        if x[j] > i and x[j + 1] < i:
            s += abs(x[j] - i) + abs(x[j + 1] - i)
        elif x[j] < i and x[j + 1] > i:
            s += abs(x[j] - i) + abs(x[j + 1] - i)
        else:
            s += abs(x[j] - x[j + 1])
    print(s, end=' ')
"""
