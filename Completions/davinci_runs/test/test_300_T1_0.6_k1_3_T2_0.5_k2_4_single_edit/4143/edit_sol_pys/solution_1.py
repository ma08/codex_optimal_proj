

def main():
    n = int(input()) # ロボットの数
    a = int(input()) # 始点
    b = int(input()) # 終点
    c = int(input()) # 始点
    d = int(input()) # 終点
    e = int(input()) # 始点

    l = [a, b, c, d, e] # 始点のリスト
    l.sort()

    if n <= l[0]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
