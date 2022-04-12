

def main():
    n = int(input())
    permutation = list(map(int, input().split()))

    lis = [permutation[0]]

    for i in range(1, n):
        if permutation[i] > lis[-1]:
            lis.append(permutation[i])

    print(len(lis))
    print(*lis)

if __name__ == '__main__':
    main()
