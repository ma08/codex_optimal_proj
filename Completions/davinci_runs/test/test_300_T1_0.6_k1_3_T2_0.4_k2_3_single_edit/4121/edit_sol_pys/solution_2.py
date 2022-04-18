

    # wall_len = int(input())
    # wall_cond = list(map(int, input().split()))
    # max_h = max(wall_cond)
    # min_h = min(wall_cond)
    # if max_h - min_h > 1:
    #     print('NO')
    # else:
    #     print('YES')
def main():
    wall_len = int(input())
    wall_cond = input()
    if wall_len == 1:
        print('YES')
        return
    for i in range(1, wall_len):
        if wall_cond[i] == '1' and wall_cond[i-1] == '0':
            print('NO')
            return
    print('YES')


if __name__ == "__main__":
    main()
