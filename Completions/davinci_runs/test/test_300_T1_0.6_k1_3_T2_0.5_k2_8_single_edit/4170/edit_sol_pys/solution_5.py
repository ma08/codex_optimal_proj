

def main():
    """
    N = int(input())
    H = list(map(int,input().split()))
    """
    N = 5
    H = [10, 4, 8, 7, 3]

    count = 0
    for i in range(N):
        if i == N - 1:
            break
            count += 1
        elif H[i] < H[i + 1]:
            break
        else:
    print(count)

if __name__ == '__main__':
    main()
