
def main():
    N, D = map(int, input().split())
    print(1 if N <= D else (N - D) // (2 * D + 1) + 1)

if __name__ == "__main__":
    main()
