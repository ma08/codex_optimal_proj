def main():
    a, b = map(int, input().split())


    print(4 * a if a == b else 2 * (a + b))

if __name__ == "__main__":
    main()
