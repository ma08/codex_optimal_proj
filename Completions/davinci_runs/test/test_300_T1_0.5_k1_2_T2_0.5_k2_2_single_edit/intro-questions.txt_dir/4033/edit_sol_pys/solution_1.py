

def main():
    a, b = map(int, input().split())

    if a == b:
        print(2 * a)
    else:
        print(a + b)

if __name__ == "__main__":
    main()
