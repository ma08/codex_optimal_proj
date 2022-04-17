
import sys

def main():
    n = int(input())
    s = input()
    if n % 2 == 1:
        print("No")
    else:
        if s[:n//2] == s[n//2:]:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
