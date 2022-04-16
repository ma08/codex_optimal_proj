
def box_packing(n, v, boxes):
    if n == 0 or len(boxes) == 0:
        return 0
    else:
        m = boxes[0]
        for box in boxes:
            if box > m:
                m = box
        boxes.remove(m)
        if m >= v:
            return m - v
        else:
            return box_packing(n-1, v, boxes)

def main():
    n, v = map(int, input().split())
    boxes = []
    for i in range(n):
        l, w, h = map(int, input().split())
        boxes.append(l*w*h)
    print(box_packing(n, v, boxes))
    
if __name__ == "__main__":
    main()
