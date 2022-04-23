

def f(x):
    while x % 10 == 0:
        x //= 10
    return x + 1


def solve(n):
    reachable = set()

    def solve(x):
        if x in reachable:
            return
        reachable.add(x)
        solve(f(x))

print(len(reachable))
