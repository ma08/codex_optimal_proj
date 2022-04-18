

def main():
    k = int(input())
    n = int(input())

    for _ in range(n):
        t, z = input().split()
        t, z = int(t), z
        if z == 'T':
            k = (k + t) % 8
        elif z == 'N':
            k = (k + 7 * t) % 8
        else:
            k = (k + 6 * t) % 8

    print(k)

main()
