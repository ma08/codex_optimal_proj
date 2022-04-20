

def main():
    wall_len = int(input())
    wall_cond = list(map(int, input().split()))  # list of wall conditions
    max_h = max(wall_cond)  # max height of wall
    min_h = min(wall_cond)  # min height of wall
    if max_h - min_h > 1:  # if diff between max and min is more than 1
        print('NO')  # then it's not possible to make the wall
    else:  # if it's possible
        print('YES')  # then print yes


if __name__ == "__main__":
    main()
