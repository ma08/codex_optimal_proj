

def main():
    n = int(input())  # number of elements
    a = [int(i) for i in input().split()]  # elements

    if n == 1:
        print(1, a[0])  # answer
        return

    a.sort()  # sort

    i = 0
    while i < n and a[i] == 0:
        i += 1  # find non-zero element

    if i == n:
        print(1, a[-1])  # answer
        return

    if i == n - 1:
        print(1, a[i])  # answer
        return

    z = a[i]  # divisor
    y = 1
    while i < n and a[i] == z:
        i += 1  # find next element

    for j in range(i, n):
        if a[j] % z != 0:
            print(1, a[j])  # answer
            return

        y = max(y, a[j] // z)  # find max of quotients

    print(y, z)  # answer


main()
