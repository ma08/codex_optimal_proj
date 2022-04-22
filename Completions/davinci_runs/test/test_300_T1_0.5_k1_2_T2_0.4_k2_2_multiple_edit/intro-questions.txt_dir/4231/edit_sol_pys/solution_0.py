

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H-h+1)*(W-w+1)) 

if __name__ == '__main__':
    main()
