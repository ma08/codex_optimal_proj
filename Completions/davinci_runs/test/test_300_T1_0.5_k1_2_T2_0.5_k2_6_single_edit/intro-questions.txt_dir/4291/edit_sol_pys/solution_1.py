
def main():
    N = int(input())
    if N % 2 == 0:
        print(N * (N - 2) // 2)
    else:
        print(N * (N - 2) // 2 + 1)


if __name__ == "__main__":
    main()
