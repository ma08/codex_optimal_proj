

def read_line():
    try:
        line = raw_input()
        return line
    except:
        return None


def read_ints():
    return [int(i) for i in read_line().split(' ')]


def main():
    N = read_ints()[0]
    A = read_ints()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] == A[j]:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
