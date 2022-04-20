

def main():
    N, M = map(int, input().split())
    foods = [0] * (M + 1)
    for i in range(N):
        K = int(input().split()[0]) - 1
        for j in range(K):
            foods[int(input().split()[0])] += 1
    print(foods.count(N))

if __name__ == '__main__':
    main()
