def main(n, a):
    for i in range(n):
        for j in range(n):
            if i * j == a:
                return i, j
    return -1, -1

if __name__ == '__main__':
    n = int(input())
    a = int(input())
    i, j = main(n, a)
    if i == -1:
        print('No')
    else:
        print('Yes')
