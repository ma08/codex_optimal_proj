

def main():
    cases = int(input())
    for _ in range(cases):
        n = int(input())
        s = input()
        x, y = 0, 0
        x_dict = {0: 0}
        y_dict = {0: 0}
        for i in range(n):
            if s[i] == 'L':
                x -= 1
            elif s[i] == 'R':
                x += 1
            elif s[i] == 'U':
                y += 1
            elif s[i] == 'D':
                y -= 1
            if x in x_dict:
                x_dict[x] = i + 1
            if y in y_dict:
                y_dict[y] = i + 1
        if x == 0 and y == 0:
            print(-1)
        else:
            l = max(x_dict[x], y_dict[y])
            r = n
            print(l, r)

if __name__ == "__main__":
    main()