

def main():
    N = int(input())
    A = list(map(int,input().split()))

    count = 0
    for i in range(N):
        if i == N - 1:
            break
        elif A[i] < A[i + 1]:
            break
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
