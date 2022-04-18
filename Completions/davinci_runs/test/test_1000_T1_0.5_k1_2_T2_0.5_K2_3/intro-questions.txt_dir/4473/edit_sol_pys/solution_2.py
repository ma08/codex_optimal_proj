#!/usr/bin/env python3

def main():
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)

if __name__ == "__main__":
    main()
