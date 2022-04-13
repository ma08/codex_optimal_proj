

def main():
    K = int(input())
    desks = list(map(int, input().split()))
    i = 0
    passes = 0
    while i < K:
        if desks[i] == i+1:
            i += 1
        passes += 1
    print(passes)

if __name__ == '__main__':
    main()
