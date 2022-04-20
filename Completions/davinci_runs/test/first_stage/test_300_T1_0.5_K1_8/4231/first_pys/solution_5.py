

def main():
    h, w = map(int, input().split())
    hh, ww = map(int, input().split())
    print((h - hh) * w + (w - ww) * hh)

if __name__ == '__main__':
    main()