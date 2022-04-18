

def main():
    h, w, x, y = [int(i) for i in input().split()]
    if h == w:
        if x == y:
            print(1)
        else:
            print(0)
    else:
        if x == y:
            print(0)
        else:
            print(1)

if __name__ == '__main__':
    main()
