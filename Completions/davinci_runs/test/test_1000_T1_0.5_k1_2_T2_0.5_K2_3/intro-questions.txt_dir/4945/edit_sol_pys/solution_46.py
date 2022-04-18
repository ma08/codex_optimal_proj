

def main():
    a, b = map(int, input().split())
    m, sum = map(int, input().split())
    maxR = 0
    for x in range(1, m // 2 + 1):
        y = (sum - 2 * x)
        if y < 1 or m < x + y:
            continue
        R = a * x + b * y
        if R > maxR:
            maxR = R
    print(maxR)

if __name__ == "__main__":
    main()
