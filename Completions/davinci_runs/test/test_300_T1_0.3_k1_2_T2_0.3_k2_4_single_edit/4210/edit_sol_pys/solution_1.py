
def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    print(sum(a) - n)

if __name__ == "__main__":
    main()
