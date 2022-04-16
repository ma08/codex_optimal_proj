

def solve(b):
    n = len(b)
    a = b[0]
    for i in range(1, n):
        if b[i] == a[0]:
            a = b[i] + a
        elif b[i] == a[-1]:
            a = a + b[i]
    return a



def main():
    t = int(input())  # read a line with a single integer
    for _ in range(t):
        b = input()  # read a list of integers, 2 in this case
        print(solve(b))


if __name__ == '__main__':
    main()
