def main():
    N = int(input())
    if N // 1000 == N % 10 and (N // 100) % 10 == (N // 10) % 10:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
