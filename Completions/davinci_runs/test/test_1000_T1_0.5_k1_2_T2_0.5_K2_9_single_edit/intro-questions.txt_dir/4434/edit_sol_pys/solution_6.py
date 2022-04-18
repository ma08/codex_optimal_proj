
def get_input():
    t = int(input())
    for i in range(t):
        n = int(input())
        yield n


def solve(n):
    if n == 1:
        return 0
    return (n - 1)**2

if __name__ == '__main__':
    for n in get_input():
        print(solve(n))
