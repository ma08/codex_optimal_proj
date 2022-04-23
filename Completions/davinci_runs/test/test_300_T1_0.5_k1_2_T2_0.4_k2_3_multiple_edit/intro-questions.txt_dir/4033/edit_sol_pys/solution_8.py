
def main():
    a, b = map(int, input().split())

    if a == b:
        print(4 * a + 1)
    else:
        print(2 * (a + b) + 1)

if __name__ == "__main__":
    main()
