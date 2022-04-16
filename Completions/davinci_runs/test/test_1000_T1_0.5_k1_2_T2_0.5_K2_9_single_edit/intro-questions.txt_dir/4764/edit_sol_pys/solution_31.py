

def main():
    n, h, v = [int(i) for i in input().split()] # input() returns string so we need to convert to int
    print(h * v * n * 4)

if __name__ == '__main__':
    main()
