

def main():
    n = int(input())
    s = [input() for i in range(n)]
    chars = 'MARCH'
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if s[i][0] in chars and s[j][0] in chars and s[k][0] in chars:
                    if len(set([s[i][0], s[j][0], s[k][0]])) == 3:
                        count += 1
    print(count)

if __name__ == '__main__':
    main()
