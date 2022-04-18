
def main():
    n = int(input())
    if n == 1:
        print(1)
    else:
        print(n + (n - 1) // 9 + 1)

if __name__ == "__main__":
    main()
