
import sys

def main():
    s = input()  # first input
    t = input()  # second input
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
