

def main():
    wall_len = int(input())
    wall_cond = list(map(int, input().split()))
    if max(wall_cond) - min(wall_cond) > 1:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    main()
