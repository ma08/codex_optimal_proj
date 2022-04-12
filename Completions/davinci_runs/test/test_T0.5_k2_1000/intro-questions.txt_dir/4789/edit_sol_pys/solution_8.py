


def swap(a, b):
    return b, a


def sort(desks):
    for i in range(len(desks)):
        for j in range(len(desks)):
            if desks[i] < desks[j]:
                desks[i], desks[j] = swap(desks[i], desks[j])
    return desks


def main():
    K = int(input())
    desks = list(map(int, input().split()))
    desks = sort(desks)
    pos = 0
    passes = 1
    while pos < K:
        for i in range(pos, K):
            if desks[i] == i+1:
                pos += 1
        passes += 1
    print(passes)


if __name__ == '__main__':
    main()
