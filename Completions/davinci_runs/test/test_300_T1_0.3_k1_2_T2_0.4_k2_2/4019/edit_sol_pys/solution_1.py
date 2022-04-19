
import sys

def main():
    n = int(input())
    s = input()
    res = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
