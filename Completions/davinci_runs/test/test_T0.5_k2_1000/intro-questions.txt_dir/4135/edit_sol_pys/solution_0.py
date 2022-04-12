

def find_divisor(n):
    for i in range(n, 0, -1):
        if n % i == 0:
            return i


def main():
    n = int(input())
    t = input()
    d = find_divisor(n)
    print(t[d:], end="")
    print(t[:d][::-1], end="")


main()
