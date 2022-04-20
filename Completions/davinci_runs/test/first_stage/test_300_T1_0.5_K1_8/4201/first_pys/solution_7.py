

def main():
    h,w,k = map(int,input().split())
    c = []
    for i in range(h):
        c.append(list(input()))

    cnt = 0
    for i in range(2**h):
        row = [0] * h
        for j in range(h):
            if (i >> j) & 1 == 1:
                row[j] = 1
        for j in range(2**w):
            col = [0] * w
            for l in range(w):
                if (j >> l) & 1 == 1:
                    col[l] = 1
            black = 0
            for m in range(h):
                for n in range(w):
                    if c[m][n] == '#' and row[m] == 1 and col[n] == 1:
                        black += 1
            if black == k:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()