

def get_input():
    n = int(input())
    a = [int(x) for x in input().split()]
    return n, a

def solve(n, a):
    return a

def main():
    n, arr = get_input()
    ans = solve(n, arr)
    print(ans)

if __name__ == '__main__':
    main()
