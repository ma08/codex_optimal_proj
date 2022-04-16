

def calc_remaining_cells(H, W, h, w, cnt):
    if (H-h) == 0 or (W-w) == 0:
        return cnt
    elif (H-h) < 0 or (W-w) < 0:
        return cnt
    else:
        cnt += (H-h)*(W-w)
        return calc_remaining_cells(H-h, W-w, h, w, cnt)

H, W = map(int, input().split())
h, w = map(int, input().split())

print(calc_remaining_cells(H, W, h, w, 0))
