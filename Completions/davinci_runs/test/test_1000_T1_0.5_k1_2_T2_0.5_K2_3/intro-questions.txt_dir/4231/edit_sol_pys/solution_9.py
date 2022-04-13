

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H*W-(H-h)*(W-w))

if __name__ == '__main__':
    main()
