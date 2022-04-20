

def main():
    wall_len = int(input())
    wall_cond = list(map(int, input().split()))
    max_h = max(wall_cond)
    min_h = min(wall_cond)
    print('YES' if max_h - min_h <= 1 else 'NO')


if __name__ == "__main__":
    main()
