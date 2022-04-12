

def main():
    K = int(input())
    desks = list(map(int, input().split()))
    pos = 1
    passes = 0
    for i in range(K):
        if desks[i] == pos:
            pos += 1
        passes += 1
    print(passes)

if __name__ == '__main__':
    main()
