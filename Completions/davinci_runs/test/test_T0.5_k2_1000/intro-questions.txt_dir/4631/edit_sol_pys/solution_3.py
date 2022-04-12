import sys

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort(reverse=True)
    y = [0] * (m + 1)
    for i in range(1, m + 1):
        y[i] = x[i % n]
        x[i % n] += 1
    print(sum(y[1:]))
    print(' '.join(map(str, y[1:])))


if __name__ == "__main__":
    main()
