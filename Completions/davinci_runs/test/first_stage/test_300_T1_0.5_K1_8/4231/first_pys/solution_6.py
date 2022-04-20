

def main():
    h, w = map(int, input().split())
    h_, w_ = map(int, input().split())
    print(h * w - (h_ * w + w_ * h - h_ * w_))


if __name__ == '__main__':
    main()