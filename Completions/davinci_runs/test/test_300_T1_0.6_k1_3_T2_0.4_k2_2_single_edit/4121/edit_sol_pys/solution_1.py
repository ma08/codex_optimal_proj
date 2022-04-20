

def main():
    wall_len = int(input())  # length of the wall
    wall_cond = list(map(int, input().split()))  # condition of the wall
    max_h = max(wall_cond)  # max height of the wall
    min_h = min(wall_cond)  # min height of the wall
    if max_h - min_h > 1:  # if max_h - min_h > 1, NO
        print('NO')
    else:  # else, YES
        print('YES')


if __name__ == "__main__":
    main()
