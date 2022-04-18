


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        curr_x, curr_y = 0, 0
        for j in range(n-1):
            if s[j] == 'L':
                curr_x -= 1
            elif s[j] == 'R':
                curr_x += 1
            elif s[j] == 'U':
                curr_y += 1
            else:
                curr_y -= 1
        if curr_x == 0 and curr_y == 0:
            print("1 1")
            continue
        curr_x, curr_y = 0, 0
        for j in range(n-1):
            if s[j] == 'L':
                curr_x -= 1
            elif s[j] == 'R':
                curr_x += 1
            elif s[j] == 'U':
                curr_y += 1
            else:
                curr_y -= 1
            if curr_x == 0 and curr_y == 0:
                print(str(j + 1) + " " + str(n))
                break
        else:
            print("-1")


if __name__ == "__main__":
    main()
