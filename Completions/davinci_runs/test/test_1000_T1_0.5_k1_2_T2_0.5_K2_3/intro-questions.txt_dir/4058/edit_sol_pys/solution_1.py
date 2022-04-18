

def get_input(n):
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    return a

def solve(a):
    ans = 0
    return ans

def main():
    n = int(input())
    a = get_input(n)
    ans = solve(a)
    print(ans)

if __name__ == '__main__':
    main()
