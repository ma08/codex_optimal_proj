
def box_packing(n, v, box):
    if n == 0:
        return 0
    else:
        m = max(box)
        box.remove(m)
        if m >= v:
            return m - v
        else:
            return box_packing(n-1, v, box)

def main():
    n, v = map(int, input().split())
    box = []
    for i in range(n):
        l, w, h = map(int, input().split())
        box.append(l*w*h)
    print(box_packing(n, v, box))

if __name__ == "__main__":
    main()
