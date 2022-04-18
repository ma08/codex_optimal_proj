import sys

def main():
    n = int(input())
    if (n % 2 == 0):
        print("Bob")
        print(n // 2)
    else:
        print("Alice")

if __name__ == "__main__":
    main()
