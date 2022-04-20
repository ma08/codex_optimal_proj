

def main():
    a, b = map(int, input().split())

    if a == b:
        print(2 * a)
    elif a > b:
        print(2 * (a - 1))
    else:
        print(2 * (b - 1))

if __name__ == "__main__":
    main()
