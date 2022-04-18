

def box_packing(n, v, boxs):
    if n == 0:
        return 0
    else:
        m = max(boxs)
        boxs.remove(m) 
        if m >= v:
            return m - v
        else:
            return box_packing(n-1, v, boxs)

def main():
    n, v = map(int, input().split())
    boxs = []
    for i in range(n):
        l, w, h = map(int, input().split())
        boxs.append(l*w*h)
    print(box_packing(n, v, boxs))

if __name__ == "__main__":
    main()
