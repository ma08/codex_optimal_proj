

def solve(input):
    n = int(input[0]) # number of elements in array
    a = [int(x) for x in input[1].split()]
    print(n)
    print(a)

    return 0


if __name__ == '__main__':
    input = [
        '5',
        '1 2 3 4 5'
    ]
    print(solve(input))
