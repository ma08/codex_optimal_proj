

def main():
    cases = int(input())
    for _ in range(cases):
        n = int(input())
        s = input()
        x, y = 0, 0
        x_dict = {0: -1}
        y_dict = {0: -1}
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
                break
        if x != 0 or y != 0:
            l = max(x_dict[x], y_dict[y]) + 1
            r = n + 1
            print(l, r - 1)

if __name__ == "__main__":
    main()
