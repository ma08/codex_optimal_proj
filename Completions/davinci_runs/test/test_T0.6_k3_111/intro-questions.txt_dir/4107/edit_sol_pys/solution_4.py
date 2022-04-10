

def main():
    n, k = map(int, input().split())
    s = input()

    def cost(l, r):
        return sum(map(int, s[l+1:r+1]))

    def f(l, r):
        if l == r:
            return 1
        if s[l] == '1' and s[r] == '1':
            return min(f(l+1, r), f(l, r-1), cost(l+k, r-k))
        if s[l] == '1':
            return min(f(l+1, r), cost(l+k, r))
        if s[r] == '1':
            return min(f(l, r-1), cost(l, r-k+1))
        return cost(l, r)

    print(f(0, n-1))

if __name__ == '__main__':
    main()
