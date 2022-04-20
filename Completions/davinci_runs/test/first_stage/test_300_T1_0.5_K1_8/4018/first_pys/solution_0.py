

def main():
    n, k = [int(i) for i in input().split()]
    s = input()
    if k > n:
        return -1
    else:
        return n*(n-1)//2 - k*(k+1)//2

if __name__ == '__main__':
    print(main())