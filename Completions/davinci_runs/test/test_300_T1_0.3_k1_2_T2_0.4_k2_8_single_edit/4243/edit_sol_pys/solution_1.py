import sys

def main():
    a = int(input())
    print(a // 500 * 1000 + a % 500 // 5 * 5)

if __name__ == "__main__":
    main()
