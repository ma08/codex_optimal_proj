

def get_input():
    n, r = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]     # 0: empty, 1: occupied
    return n, r, a

def solve(n, r, a):
    ans = 0
    i = 1
    while i <= n:
        if a[i-1] == 0:
            j = i
            while j <= n and a[j-1] == 0:
                j += 1
            if j - i + 1 > 2*r:     # too many empty rooms
                return -1
            if j <= n:
                a[j-1] = 1     # occupy the room
                ans += 1
            else:
                return -1     # no occupied room after the current empty room
            i = j
        else:
            i += 1
    return ans

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
