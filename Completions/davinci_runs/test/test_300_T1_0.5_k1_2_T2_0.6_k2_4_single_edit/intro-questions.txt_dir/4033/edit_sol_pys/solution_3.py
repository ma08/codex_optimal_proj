

def main():
    a, b = (int(x) for x in input().split())

    if a == b:
        print(4 * a)
    else:
        print(2 * (a + b))

if __name__ == "__main__":
    main()
