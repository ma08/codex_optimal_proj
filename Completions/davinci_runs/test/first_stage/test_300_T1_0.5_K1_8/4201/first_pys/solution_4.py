

def main():
    h, w, k = map(int, input().split())
    c = [list(input()) for i in range(h)]
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            tmp = 0
            for x in range(h):
                for y in range(w):
                    if (i >> x) & 1 and (j >> y) & 1:
                        if c[x][y] == '#':
                            tmp += 1
            if tmp == k:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()