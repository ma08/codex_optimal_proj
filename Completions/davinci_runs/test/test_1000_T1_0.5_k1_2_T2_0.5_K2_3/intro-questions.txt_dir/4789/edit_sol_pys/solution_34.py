


def main():
    K = int(input())
    desks = list(map(int, input().split()))  # 受験者の位置
    pos = 0
    passes = 0
    while pos < K-1:
        if desks[pos] == pos + 1:
            pos += 1
            passes += 1
        elif desks[pos] > pos + 1:
            pos += desks[pos] - pos - 1
            passes += 1
        else:
            pos += 1
            passes += 1

    print(passes)

if __name__ == '__main__':
    main()
