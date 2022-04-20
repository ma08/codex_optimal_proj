

def main():
    n, x, y = map(int, input().split())
    binary = input()
    if (int(binary[:x], 2) % 10**x) == 10**y:
        print(0)
    else:
        print(1)

if __name__ == "__main__":
    main()