

def main():
    h, w = map(int, input().split())  # type: int, int

    if h % 3 == 0 or w % 3 == 0:
        print(0)
        return

    if h > w:
        h, w = w, h

    min_diff = float('inf')
    for i in range(1, h):
        area_1 = i * w  # type: int
        area_2 = (h - i) // 2 * w  # type: int
        area_3 = (h - i) - area_2  # type: int
        max_area = max(area_1, area_2, area_3)  # type: int
        min_area = min(area_1, area_2, area_3)  # type: int
        min_diff = min(min_diff, max_area - min_area)

    print(min_diff)


if __name__ == '__main__':
    main()
