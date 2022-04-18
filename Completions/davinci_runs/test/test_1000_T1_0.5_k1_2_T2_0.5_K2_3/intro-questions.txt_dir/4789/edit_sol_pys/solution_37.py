

def main():
    K = int(input())
    desks = list(map(int, input().split()))
    pos = 1
    passes = 0
    while pos <= K:
        if desks[pos-1] == pos:
            pos += 1
        else:
            desks[pos-1], desks[desks[pos-1]-1] = desks[desks[pos-1]-1], desks[pos-1]
        passes += 1
    print(passes)

if __name__ == '__main__':
    main()
