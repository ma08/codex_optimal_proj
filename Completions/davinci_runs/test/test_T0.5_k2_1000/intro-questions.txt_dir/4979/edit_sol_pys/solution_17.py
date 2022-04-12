

def main():
    n = int(input())
    print(int(bin(n)[2:][::-1], 2))  # bin() returns the binary representation of an integer


if __name__ == "__main__":
    main()
