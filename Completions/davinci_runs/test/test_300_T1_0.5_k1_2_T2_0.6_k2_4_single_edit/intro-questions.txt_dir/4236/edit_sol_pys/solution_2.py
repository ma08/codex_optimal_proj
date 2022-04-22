

def f(n, m):
    left = [0] * (m + 1)
    right = [0] * (m + 1)

    for i in range(n):
        l, r = map(int, input().split())
        left[l] += 1
        right[r] += 1

    counter = 0
    for i in range(1, m + 1):
        if left[i] == right[i]:
            counter += 1
        elif left[i] > right[i]:
            print(counter)
            break
    else:
        print(counter)


if __name__ == '__main__':
    n, m = map(int, input().split())
    f(n, m)
