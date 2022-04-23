def takahashi_traveling(x, k, d):  # x: 位置、k: 移動回数、d: 移動距離
    if k <= (x // d):  # 同じ方向に移動し続ける
        return x - k * d  # 同じ方向に移動し続ける
    else:  # 移動方向を変える
        return abs(x - d * ((x // d) + 1))  # 移動方向を変える

if __name__ == '__main__':
    x, k, d = map(int, input().rstrip().split())
    print(takahashi_traveling(x, k, d))


"""
Takahashi is now at coordinate 6. It is optimal to make the following moves:
 - Move from coordinate 6 to (6 - 4 =) 2.
 - Move from coordinate 2 to (2 - 4 =) -2.
Here, the absolute value of the coordinate of the destination is 2, and we cannot make it smaller.
"""
def takahashi_traveling(x, k, d):
    if k <= (x // d):
        return x - k * d
    else:
        return abs(x - d * ((x // d) + 1))

if __name__ == '__main__':
    x, k, d = map(int, input().rstrip().split())
    print(takahashi_traveling(x, k, d))
