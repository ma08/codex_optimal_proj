import sys

def main():
    N = int(input())
    print(N // 500 * 1000 + N % 500 // 5 * 5)

if __name__ == "__main__":
    main()
