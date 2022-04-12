
import sys

def main():
    n = int(input())
    for i in range(n):
        s = input()
        t = input()
        count = 0
        for j in range(len(s)):
            if s[j] != t[j]:
                count += 1
        print(count)

if __name__ == '__main__':
    main()
