
def main():
    n = int(input())
    print(int(bin(n)[2:][::-1],2))

if __name__ == "__main__":
    main()
