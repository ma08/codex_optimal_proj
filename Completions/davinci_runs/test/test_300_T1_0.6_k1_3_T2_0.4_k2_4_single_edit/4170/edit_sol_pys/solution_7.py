

def main():
    """
    N = int(input())
    H = list(map(int,input().split()))
    """
    N = 5
    H = [10, 4, 8, 7, 3]

    count = 1
    for i in range(N):
        if i == N - 1:
            break
        elif H[i] < H[i + 1]:
            break
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
