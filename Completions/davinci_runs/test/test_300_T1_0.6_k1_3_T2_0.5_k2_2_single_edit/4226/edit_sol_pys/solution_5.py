

def main():
    x, y = map(int, input().split())
    if x < y//2:
        print(y-2*x)
    else:
        print(0)

if __name__ == '__main__':
    main()
