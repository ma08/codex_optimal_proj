

def main():
    n = int(input())
    t_s = [list(map(int, input().split())) for _ in range(n)]
    t_s.append([0, 0])

    for i in range(n):
        t, x, y = t_s[i+1][0] - t_s[i][0], t_s[i+1][1] - t_s[i][1], t_s[i+1][2] - t_s[i][2]
        if (x + y) > t or (x + y) % 2 != t % 2:
            print('No')
            exit()

    print('Yes')

if __name__ == '__main__':
    main()
