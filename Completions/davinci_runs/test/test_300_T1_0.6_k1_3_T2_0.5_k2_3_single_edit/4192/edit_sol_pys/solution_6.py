

def main():
    d, t, s = map(int, input().split())

    if d/s <= t:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
