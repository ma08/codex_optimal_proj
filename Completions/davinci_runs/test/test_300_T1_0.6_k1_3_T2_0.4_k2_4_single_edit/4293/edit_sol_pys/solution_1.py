

def main():
    p, q, r = map(int, input().split())

    print(min(p + q, q + r, r + p))


if __name__ == '__main__':
    main()
