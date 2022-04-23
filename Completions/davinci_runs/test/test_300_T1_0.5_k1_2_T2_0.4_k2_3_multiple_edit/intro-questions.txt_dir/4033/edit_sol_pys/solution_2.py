#!/usr/bin/env python3

def main():
    a, b = map(int, input().split())  # 入力を受け取る

    if a == b:
        print(4 * a)  # 同じならば4倍
    else:
        print(2 * (a + b))

if __name__ == "__main__":
    main()
