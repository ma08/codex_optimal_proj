

def main():
    K, N = map(int, input().split())
    desks = list(map(int, input().split()))
    # print(desks)
    # pos = 0
    # passes = 0
    # while pos < K:
    #     for i in range(pos, K):
    #         if desks[i] == i+1:
    #             pos += 1
    #     passes += 1
    # print(passes)
    for i in range(K):
        print(desks[i])

if __name__ == '__main__':
    main()
