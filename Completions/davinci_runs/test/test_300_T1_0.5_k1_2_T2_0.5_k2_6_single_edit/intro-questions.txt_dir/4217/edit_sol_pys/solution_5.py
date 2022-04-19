

def solve(n, m):
    foods = [0] * m
    for i in range(n):
        k = int(input().split()[0])
        for j in map(int, input().split()):
            foods[j-1] += 1
    return foods.count(n)

def main():
    n, m = map(int, input().split())
    print(solve(n, m))

if __name__ == '__main__':
    main()
