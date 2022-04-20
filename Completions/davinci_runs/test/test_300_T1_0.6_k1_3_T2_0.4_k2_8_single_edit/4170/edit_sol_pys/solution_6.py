

def main():
    """
    N = int(input())
    H = list(map(int,input().split()))
    """
    N = 3
    H = [10, 4, 8]

    count = 0
    for i in range(N - 1):
        if H[i] < H[i + 1]:
            break
        elif H[i] < H[i + 1]:
            break
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
