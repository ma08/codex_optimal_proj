

def box_packing(v, boxes):
    if v == 0:
        return 1
    if v < 0:
        return 0
    if len(boxes) == 0:
        return 0
    return box_packing(v - max(boxes), boxes) + box_packing(v, boxes[:-1])

def main():
    n, v = map(int, input().split())
    boxes = []
    for i in range(n):
        l, w, h = map(int, input().split())
        boxes.append(l*w*h)
    print(box_packing(v, boxes))

if __name__ == "__main__":
    main()
