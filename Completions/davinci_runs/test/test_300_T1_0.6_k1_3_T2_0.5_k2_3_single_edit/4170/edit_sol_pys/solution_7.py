

def main():
    """
    N = int(input())
    H = list(map(int,input().split()))
    """
    N = 6
    H = [10, 4, 8, 7, 3, 15]

    count = 0
    for i in range(1, N):
        if H[i - 1] >= H[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
