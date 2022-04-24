

h, w = map(int, input().split())  # h: 下穴の縦幅, w: 下穴の横幅
h_, w_ = map(int, input().split())  # h_: 小石の縦幅, w_: 小石の横幅

print((h - h_) * (w - w_))
