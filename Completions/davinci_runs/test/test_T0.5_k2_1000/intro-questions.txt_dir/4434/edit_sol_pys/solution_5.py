
def get_input():
    t = int(input())
    for i in range(t):
        n = int(input())
        yield n, i

def solve(n, i):
    if n == 1:
        return 0
    return (n - 1)**2

if __name__ == '__main__':
    for n, i in get_input():
        print("Case #{}: {}".format(i + 1, solve(n, i)))
