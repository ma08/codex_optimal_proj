def main():
    a, b, c = map(int, input().split())
    i, j, k = map(int, input().split())
    x = min(a / i, b / j, c / k)
    print("{:.6f} {:.6f} {:.6f}".format(a - x * i, b - x * j, c - x * k))


main()
