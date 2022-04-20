

def main():
    n = int(input())
    f = list(map(int, input().split()))

    # find all the zeros
    zeros = []
    for i in range(n):
        if f[i] == 0:
            zeros.append(i)

    # assign the zeros to the non-zeros
    for i in range(len(zeros)):
        f[zeros[i]] = i + 1

    print(' '.join(map(str, f)))

if __name__ == '__main__':
    main()
