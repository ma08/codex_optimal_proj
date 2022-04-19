

def main():
    n = int(input())
    ans = [0 for i in range(n)]
    s = input()
    if (n == 1):
        ans[0] = 1
        print(1)  # number of operations
        print(1)  # sequence of operations
        return
    if (n == 2):
        if (s[0] < s[1]):
            ans[0] = 1
            ans[1] = 1
            print(1)  # number of operations
            print(1, 1)  # sequence of operations
        else:
            ans[0] = 2
            ans[1] = 1
            ans[2] = 2
            print(2)  # number of operations
            print(1, 2)  # sequence of operations
        return
    if (n == 3):
        if (s[0] < s[1] and s[1] < s[2]):
            ans[0] = 1
            ans[1] = 1
            ans[2] = 1
            ans[3] = 1
            print(1)  # number of operations
            print(1, 1, 1)  # sequence of operations
        elif (s[0] < s[1] and s[1] > s[2]):
            ans[0] = 2
            ans[1] = 1
            ans[2] = 2
            ans[3] = 1
            print(2)  # number of operations
            print(1, 2, 1)  # sequence of operations
        elif (s[0] > s[1] and s[1] < s[2]):
            ans[0] = 2
            ans[1] = 2
            ans[2] = 1
            ans[3] = 1
            print(2)  # number of operations
            print(2, 1, 1)  # sequence of operations
        else:
            ans[0] = 3
            ans[1] = 1
            ans[2] = 2
            ans[3] = 3
            print(3)  # number of operations
            print(1, 2, 3)  # sequence of operations
        return
    if (s[0] == s[1]):
        ans[0] = 1
        ans[1] = 1
        ans[2] = 1
        ans[3] = 1
        ans[4] = 1
        ans[5] = 1
        ans[6] = 1
        ans[7] = 1
        ans[8] = 1
        print(1)  # number of operations
        print(1, 1, 1, 1, 1, 1, 1, 1, 1)  # sequence of operations
        return
    if (s[0] < s[1]):
        ans[0] = 1
        ans[1] = 1
        ans[2] = 1
        ans[3] = 1
        ans[4] = 1
        ans[5] = 1
        ans[6] = 1
        ans[7] = 1
        print(1)  # number of operations
        print(1, 1, 1, 1, 1, 1, 1, 1)  # sequence of operations
        return
    if (s[1] < s[2]):
        ans[0] = 1
        ans[1] = 2
        ans[2] = 1
        ans[3] = 1
        ans[4] = 1
        ans[5] = 1
        ans[6] = 1
        ans[7] = 1
        print(1)  # number of operations
        print(2, 1, 1, 1, 1, 1, 1, 1)  # sequence of operations
        return
    if (s[2] < s[3]):
        ans[0] = 1
        ans[1] = 2
        ans[2] = 2
        ans[3] = 1
        ans[4] = 1
        ans[5] = 1
        ans[6] = 1
        ans[7] = 1
        print(1)  # number of operations
        print(2, 2, 1, 1, 1, 1, 1, 1)  # sequence of operations
        return
    if (s[3] < s[4]):
        print(1)
        print(2, 2, 2, 1, 1, 1, 1, 1)
        return
    if (s[4] < s[5]):
        print(1)
        print(2, 2, 2, 2, 1, 1, 1, 1)
        return
    if (s[5] < s[6]):
        print(1)
        print(2, 2, 2, 2, 2, 1, 1, 1)
        return
    if (s[6] < s[7]):
        print(1)
        print(2, 2, 2, 2, 2, 2, 1, 1)
        return
    if (s[7] < s[8]):
        print(1)
        print(2, 2, 2, 2, 2, 2, 2, 1)
        return
    print(2)
    print(1, 2, 1, 2, 1, 2, 1, 2, 1)
    return

if __name__ == "__main__":
    main()
