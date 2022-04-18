
def main():
    n, h, v = [int(x) for x in input().split(' ')]
    print((n - max(h, n - h)) * (n - max(v, n - v)) * 4)

if __name__ == "__main__":
    main()
