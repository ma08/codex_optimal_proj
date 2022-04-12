
def box_pack(n, v, boxes):
    if n == 0:
        return 0
    else:
        m = max(boxes)
        if m >= v:
            boxes.remove(m)
            return m - v
        else:
            return box_pack(n-1, v, boxes)

def main():
    n, v = map(int, input().split())
    boxes = []
    for i in range(n):
        l, w, h = map(int, input().split())
        boxes.append(l*w*h)
    print(box_pack(n, v, boxes))

if __name__ == "__main__":
    main()
