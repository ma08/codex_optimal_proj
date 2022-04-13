

def solver(n, a):
    if len(set(a)) == 1:
        return 'YES'
    if len(set(a)) == 2:
        if a.count(max(set(a))) == 1:
            return 'YES'
        else:
            return 'NO'
    if len(set(a)) > 2:
        return 'NO'


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solver(n, a))
