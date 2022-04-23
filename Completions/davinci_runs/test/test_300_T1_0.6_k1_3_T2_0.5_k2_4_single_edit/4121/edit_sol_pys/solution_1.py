#!/usr/bin/env python3

def main():
    wall_len = int(input())
    wall_cond = list(map(int, input().split()))
    max_h = max(wall_cond)
    min_h = min(wall_cond)
    if max_h - min_h > 1:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    main()
