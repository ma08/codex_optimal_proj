

def main():
    h, w = map(int, input().split())
    h2, w2 = map(int, input().split())
    print((h-h2)*w+(w-w2)*h-h*w)

if __name__ == '__main__':
    main()