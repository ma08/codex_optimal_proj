

def main():
    wall_len = int(input())
    wall_cond = [int(i) for i in input().split()]
    max_h = max(wall_cond)  # находим максимальную высоту стены
    min_h = min(wall_cond)  # находим минимальную высоту стены
    if max_h - min_h > 1:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    main()
