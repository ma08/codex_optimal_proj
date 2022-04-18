

def main():
    k = int(input())
    n = int(input())

    for _ in range(n):
        t, z = input().split()[:2]
        t = int(t)
        if z == 'T':
            k = (k + 1) % 8
        elif z == 'N':
            k = (k + 7) % 8
        else:
            k = (k + 6) % 8

    print(k)

main()
