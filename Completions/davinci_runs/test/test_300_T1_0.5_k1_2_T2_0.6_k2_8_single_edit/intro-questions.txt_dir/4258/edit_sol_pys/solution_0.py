
def main():
    A, B, T = map(int, input().split())  # A:初期位置、B:移動距離、T:時間
    print(B * (T // A + 1))


if __name__ == '__main__':
    main()
