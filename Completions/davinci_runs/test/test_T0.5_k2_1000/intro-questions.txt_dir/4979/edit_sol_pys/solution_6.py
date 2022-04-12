

def main():
    n = int(input())
    print(int(bin(n)[2:][::-1], 2))  # [2:] to remove 0b and [::-1] to reverse the string.

if __name__ == "__main__":
    main()
