

def find_minimum_heaters(n, r, a):
    if n < r:
        return -1

    heaters = 0
    for i in range(len(a)):
        if a[i] == 0:
            if i >= r and a[i-r] == 0:
                if i + r < len(a) and a[i+r] == 0:
                    return -1
                else:
                    heaters += 1
                    a[i] = 1
                    a[i-r+1:i+1] = [1] * (r-1)
                    if i + r < len(a):
                        a[i+1:i+r+1] = [1] * r
            elif i + r < len(a) and a[i+r] == 0:
                heaters += 1
                a[i] = 1
                a[i+1:i+r+1] = [1] * r
    return heaters


def run_tests():
    n, r = 6, 2
    a = [0, 1, 1, 0, 0, 1]
    assert find_minimum_heaters(n, r, a) == 3

    n, r = 5, 3
    a = [1, 0, 0, 0, 1]
    assert find_minimum_heaters(n, r, a) == 2

    n, r = 5, 10
    a = [0, 0, 0, 0, 0]
    assert find_minimum_heaters(n, r, a) == -1

    n, r = 10, 3
    a = [0, 0, 1, 1, 0, 1, 0, 0, 0, 1]
    assert find_minimum_heaters(n, r, a) == 3


if __name__ == '__main__':
    run_tests()
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(find_minimum_heaters(n, r, a))