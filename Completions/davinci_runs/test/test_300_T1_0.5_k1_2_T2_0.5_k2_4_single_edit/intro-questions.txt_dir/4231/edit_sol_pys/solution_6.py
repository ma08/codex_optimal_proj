

def calc_remaining_cells(n, m, c_list):
    if c_list[m-1] > c_list[0]/2:
        return 0
    
    cnt = 0
    tmp = 0
    for i in range(n):
        if tmp + c_list[i] > c_list[0]/2:
            cnt += 1
            tmp = 0
        tmp += c_list[i]
    return cnt + 1

H, W = map(int, input().split())
h, w = map(int, input().split())

print(calc_remaining_cells(H, W, h, w))
