

def main():
    n, k = map(int, input().split())
    S = input()
    print(S*(k//n) + S[:k%n])

if __name__ == "__main__":
    main()
