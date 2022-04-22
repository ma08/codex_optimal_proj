
def main():
    H, W = map(int, input().split())
    A, B = map(int, input().split())
    print(H*W-(H-A)*(W-B))

if __name__ == '__main__':
    main()
