


def box_packing(n, volume, boxes):
    if n == 0:
        return 0
    else:
        m = max(boxes)
        boxes.remove(m)
        if m >= volume:
            return m - volume
        else:
            return box_packing(n - 1, volume, boxes)


def main():
    n, volume = map(int, input().split())
    boxes = []
    for i in range(n):
        l, w, h = map(int, input().split())
        boxes.append(l * w * h)
    print(box_packing(n, volume, boxes))


if __name__ == "__main__":
    main()
