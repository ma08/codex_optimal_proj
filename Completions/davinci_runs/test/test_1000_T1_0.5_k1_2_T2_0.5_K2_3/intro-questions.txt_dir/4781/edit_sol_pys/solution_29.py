
def main():
    k = int(input())
    n = int(input())

    for _ in range(n):
        t, z = input().split()
        t, z = int(t), z
        if z == 'T':
            k = (k + 1) % 8
        elif z == 'F':
            k = (k + 7) % 8
        elif z == 'L':
            k = (k + 3) % 8
        elif z == 'R':
            k = (k + 5) % 8
        elif z == 'B':
            k = (k + 6) % 8

    print(k)

main()
