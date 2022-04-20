

def main():
    """
    N = int(input())
    H = list(map(int,input().split()))
    """
    N = 5
    H = [10, 4, 8, 7, 3]

    # count = 0
    for i in range(N):
        if i != N - 1 and H[i] > H[i + 1]:
            H[i] -= 1
    print(sum(H))

if __name__ == '__main__':
    main()
