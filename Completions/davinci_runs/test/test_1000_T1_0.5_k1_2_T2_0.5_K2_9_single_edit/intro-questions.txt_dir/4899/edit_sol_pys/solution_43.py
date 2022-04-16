#!/usr/bin/env python3


def main():
    greeting = input().strip()
    new_greeting = greeting.replace('e', 'ee', 1)
    print(new_greeting)


if __name__ == '__main__':
    main()
