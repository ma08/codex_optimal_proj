

def box_packing(n, v, boxes): 
    if n == 0:
        return 0
    else:
        m = max(boxes)
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
