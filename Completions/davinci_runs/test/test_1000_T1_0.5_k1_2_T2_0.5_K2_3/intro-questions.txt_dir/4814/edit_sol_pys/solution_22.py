
def solve(n, names):
    if names == sorted(names):
        print("INCREASING")
    elif names == sorted(names, reverse=True):
        print("DECREASING")
    else:
        print("NEITHER")

if __name__ == '__main__':
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input())
    solve(n, names)
