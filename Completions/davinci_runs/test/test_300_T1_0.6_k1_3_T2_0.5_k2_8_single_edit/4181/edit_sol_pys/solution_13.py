

def main(n, m):
    array = list(range(1, n+1))
    idx = 0
    while len(array) != 1:
        idx = (idx + m - 1) % len(array)
        array.pop(idx)

    return array[0]

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    print(main(n, m))
