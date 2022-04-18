

def main():
    K = int(input())
    desks = list(map(int, input().split()))
    # print(desks)
    pos = 1
    passes = 0
    while pos <= K:
        if desks[pos-1] == pos:
            pos += 1
        else:
            passes += 1
            pos = 1
    print(passes)

if __name__ == '__main__':
    main()
