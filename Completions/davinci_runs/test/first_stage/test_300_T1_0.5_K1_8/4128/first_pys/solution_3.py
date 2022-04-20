

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n % 2 == 0:
            print(int(n / 2))
        else:
            print(0)


if __name__ == "__main__":
    main()