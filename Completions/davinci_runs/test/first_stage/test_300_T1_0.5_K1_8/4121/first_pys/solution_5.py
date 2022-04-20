

def solve(n, a):
    a = list(map(int, a))
    if len(set(a)) == 1:
        return 'YES'
    if n == 2:
        return 'NO'
    if max(a) - min(a) > 2:
        return 'NO'
    if max(a) - min(a) == 2:
        if a.count(max(a)) > 1 and a.count(min(a)) > 1:
            return 'NO'
        return 'YES'
    if max(a) - min(a) == 1:
        if a.count(max(a)) > 1 or a.count(min(a)) > 1:
            return 'NO'
        return 'YES'



def main():
    n = int(input())
    a = input().split()
    print(solve(n, a))


if __name__ == '__main__':
    main()