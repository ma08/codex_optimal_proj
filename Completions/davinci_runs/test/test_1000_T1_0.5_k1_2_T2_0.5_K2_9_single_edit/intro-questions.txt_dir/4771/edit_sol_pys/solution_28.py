

def box_packing(n, v):
    boxes = []
    for i in range(n):
        l, w, h = map(int, input().split())
        boxes.append(l*w*h)
    boxes.sort()
    boxes.reverse()
    total = 0
    for i in range(n):
        total += boxes[i]
        if total >= v:
            return total - v
    return total - v

def main():
    n, v = map(int, input().split())
    print(box_packing(n, v))

if __name__ == "__main__":
    main()
