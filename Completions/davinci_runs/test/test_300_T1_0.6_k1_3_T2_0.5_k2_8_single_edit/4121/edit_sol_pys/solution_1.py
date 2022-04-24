

def main():
    wall_len = int(input())  # длина стены
    wall_cond = list(map(int, input().split()))  # высота стены
    max_h = max(wall_cond)  # максимальная высота
    min_h = min(wall_cond)  # минимальная высота
    if max_h - min_h > 1:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    main()
