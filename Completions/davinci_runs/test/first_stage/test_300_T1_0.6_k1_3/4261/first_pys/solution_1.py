


def main():
    a, b, c = map(int, input().split())
    print("{}".format(c - min(a-b, c)))

if __name__ == "__main__":
    main()