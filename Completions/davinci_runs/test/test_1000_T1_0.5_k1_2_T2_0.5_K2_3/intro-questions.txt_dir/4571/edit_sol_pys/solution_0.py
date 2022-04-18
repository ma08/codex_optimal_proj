

def main():
    N, M = map(int, input().split())
    success_prob = 1
    for i in range(M):
        success_prob /= 2
    print(int(1900 * M * success_prob + 100 * (N - M)))

if __name__ == '__main__':
    main()
