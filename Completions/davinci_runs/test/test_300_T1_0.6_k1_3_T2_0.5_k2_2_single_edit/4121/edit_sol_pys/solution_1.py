

def main():
    n = int(input())
    wall = list(map(int, input().split()))
    max_h = max(wall)
    min_h = min(wall)
    if (max_h - min_h) > 1:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    main()
