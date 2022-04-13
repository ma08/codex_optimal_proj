

def main():
    K, N = map(int, input().split())
    desks = list(map(int, input().split()))
    pos = 1
    passes = 0
    while pos < K:
        if desks[pos-1] == pos:
            pos += 1
            passes += 1
        else:
            pos = desks[pos-1]
    print(passes)

if __name__ == '__main__':
    main()
