

def main():
    a, b = map(int, raw_input().split())

    if a == b:
        print(4 * a)
    else:
        print(2 * (a + b))

if __name__ == "__main__":
    main()
