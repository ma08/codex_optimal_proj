
s = input()

def get_min_diff(s):
    min_diff = 10000
    for i in range(len(s) - 2): # 繰り返し回数を指定
        x = int(s[i:i+3]) # 文字列を整数型に変換
        diff = abs(x - 753)
        if diff < min_diff:
            min_diff = diff
    return min_diff

print(get_min_diff(s))
