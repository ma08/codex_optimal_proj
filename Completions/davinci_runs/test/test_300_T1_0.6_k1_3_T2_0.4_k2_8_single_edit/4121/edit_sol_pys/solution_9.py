

def main():
    wall_len = int(input())
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for i in wall_cond:
        if i == 1:
            count_1 += 1
        elif i == 2:
            count_2 += 1
        elif i == 3:
            count_3 += 1
    if count_1 > 0 and count_2 > 0 and count_3 > 0:
        print('NO')
        return
    wall_cond = list(map(int, input().split()))
    max_h = max(wall_cond)
    min_h = min(wall_cond)
    if max_h - min_h >= 2:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    main()
