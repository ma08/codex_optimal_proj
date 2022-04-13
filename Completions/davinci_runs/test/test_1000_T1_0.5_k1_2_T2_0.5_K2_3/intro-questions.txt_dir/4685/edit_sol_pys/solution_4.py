#!/usr/bin/env python3

def main():
    print(max(map(int, input().split())) * (2**int(input())))

if __name__ == '__main__':
    main()
