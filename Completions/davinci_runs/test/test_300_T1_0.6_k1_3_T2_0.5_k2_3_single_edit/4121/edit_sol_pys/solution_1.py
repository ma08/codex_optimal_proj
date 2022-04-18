

def main():
    wall_len = int(input())
    wall_cond.sort()
    wall_cond = list(map(int, input().split()))
    max_h = max(wall_cond)
    min_h = min(wall_cond)
    if max_h - min_h > 1 or wall_cond[0] == 0 and wall_cond[-1] == 2:
    elif wall_cond[0] == 0 and wall_cond[-1] == 1:
        if wall_len % 2 == 0:
            print('YES')
        else:
            print('NO')
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    main()
