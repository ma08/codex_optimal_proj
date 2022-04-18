

def main():
    K = int(input())
    desks = list(map(int, input().split()))
    print(desks)
    pos = 0
    passes = 0
    while pos < K:
        for i in range(pos, K):
            if desks[i] == i+1:
                pos += 1
        passes += 1
    print(passes)

if __name__ == '__main__':
    main()
