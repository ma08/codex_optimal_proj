
def main():
    H, W = map(int, input().split())  # 行と列
    h, w = map(int, input().split())  # 切り取る行と列
    print(H*W-(H-h)*(W-w))  # 切り取らない部分だけ

if __name__ == '__main__':
    main()
