
def solve(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return n - 2

def main():
    n = int(input())
    print(solve(n))

if __name__ == '__main__':
    main()
