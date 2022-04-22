
def main():
    a, b, c, d, e, f, g, h = map(int, input().split())
    print(max(a * c, a * d, b * c, b * d, e * g, e * h, f * g, f * h))

if __name__ == '__main__':
    main()
