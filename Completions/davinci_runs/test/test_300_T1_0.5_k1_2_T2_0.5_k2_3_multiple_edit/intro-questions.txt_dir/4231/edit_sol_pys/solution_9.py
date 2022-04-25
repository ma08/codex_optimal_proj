
def main():
    H, W = map(int, input().split())  # 行列のサイズ
    h, w = map(int, input().split())  # 白いマスのサイズ
    print(H*W-(H-h)*(W-w))  # 白いマスの個数

if __name__ == '__main__':
    main()
