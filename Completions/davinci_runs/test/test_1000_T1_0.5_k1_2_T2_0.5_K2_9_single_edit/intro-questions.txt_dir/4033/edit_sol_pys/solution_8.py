

def main():
    a, b = map(int, input().split())

    if a == b:
        print(str(4 * a))
    else:
        print(str(2 * (a + b)))

if __name__ == "__main__":
    main()
