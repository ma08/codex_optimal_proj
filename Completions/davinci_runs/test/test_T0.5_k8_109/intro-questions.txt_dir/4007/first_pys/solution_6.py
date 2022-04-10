

def main():
    n = int(input())
    f = list(map(int, input().split()))
    f = [0 if x == 0 else x for x in f]
    i = 1
    while i <= n:
        if i not in f:
            f[f.index(0)] = i
        i += 1
    f = [str(x) for x in f]
    print(' '.join(f))

main()