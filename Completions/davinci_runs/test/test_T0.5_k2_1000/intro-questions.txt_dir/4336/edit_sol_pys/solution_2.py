def main():
    # input
    W, H, x, y = map(int, input().split())
    # compute
    if x == 0 or x == W or y == 0 or y == H or x == W/2 or y == H/2:
        print(W*H/2, 1, sep=' ')
    else:
        print(W*H/2, 0, sep=' ')

if __name__ == '__main__':
    main()
