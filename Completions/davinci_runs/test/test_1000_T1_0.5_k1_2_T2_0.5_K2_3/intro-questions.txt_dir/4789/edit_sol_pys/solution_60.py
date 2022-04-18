

def main():
    K = int(input())
    desks = list(map(int, input().split()))
    pos = 0
    passes = 0
    while pos < K:
        if desks[pos] == pos+1:
        else:
            pos = desks[pos]-1
            pos += 1
        passes += 1
    print(passes)

if __name__ == '__main__':
    main()
