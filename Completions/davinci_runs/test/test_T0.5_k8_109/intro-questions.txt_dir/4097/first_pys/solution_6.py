

def main():
    n = int(input())
    b = [int(i) for i in input().split()]

    if n == 1:
        print(0)
        return

    if n == 2:
        if b[0] == b[1]:
            print(0)
            return
        else:
            print(1)
            return

    d = b[1] - b[0]
    used = [0] * n
    for i in range(1, n):
        if b[i] - b[i - 1] != d:
            if b[i] - b[i - 1] == d - 1:
                if used[i - 1] == 0:
                    used[i - 1] = 1
                    b[i - 1] += 1
                else:
                    print(-1)
                    return
            elif b[i] - b[i - 1] == d + 1:
                if used[i] == 0:
                    used[i] = 1
                    b[i] -= 1
                else:
                    print(-1)
                    return
            else:
                print(-1)
                return

    print(sum(used))

if __name__ == "__main__":
    main()