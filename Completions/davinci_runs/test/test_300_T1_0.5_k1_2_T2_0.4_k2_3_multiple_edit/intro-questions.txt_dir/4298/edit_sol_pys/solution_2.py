
def main():
    N, D = map(int, input().split())
    print((N - D) // (2 * D + 1) + 1)

if __name__ == "__main__":
    main()
