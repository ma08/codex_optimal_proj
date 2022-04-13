

def main():
    n = int(input())  # number of elements in list
    a = [int(i) for i in input().split()]  # elements of list

    a.sort()  # sorting the list

    if n == 1:
        print(1, a[0])  # if there is only one element in list
        return  # return

    i = 0
    while i < n and a[i] == 0:  # skipping zeros
        i += 1

    if i == n:
        print(1, a[-1])
        return

    if i == n - 1:
        print(1, a[i])
        return

    z = a[i]
    y = 1
    while i < n and a[i] == z:
        i += 1

    for j in range(i, n):
        if a[j] % z != 0:
            print(1, a[j])
            return

        y = max(y, a[j] // z)

    print(y, z)


main()
