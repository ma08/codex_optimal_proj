#! /usr/bin/env python3


def main():
    s = input()
    t = input()

    sticky = []
    for i in range(len(s)):
        if s[i] != t[i]:
            sticky.append(s[i])

    print("".join(set(sticky)))

if __name__ == '__main__':
    main()
