
def main():
    n, k = map(int, input().split())
    s = input()
    print(s*(k//n) + s[:k%n])

if __name__ == "__main__":
    main()
