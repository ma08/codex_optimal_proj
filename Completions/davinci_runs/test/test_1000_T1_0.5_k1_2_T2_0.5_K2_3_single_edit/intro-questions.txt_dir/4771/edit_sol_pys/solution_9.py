

def box_packing(n, v, boxes):
    if n == 0:
        return 0
    else:
        m = max(boxes) # find the max volume box
        boxes.remove(m) # remove the max volume box
        if m >= v:
            return m - v
        else:
            return box_packing(n-1, v, boxes)

def main():
    n, v = map(int, input().split()) # get the number of boxes, volume of the box
    boxes = []
    for i in range(n):
        l, w, h = map(int, input().split())
        boxes.append(l*w*h)
    print(box_packing(n, v, boxes))

if __name__ == "__main__":
    main()
