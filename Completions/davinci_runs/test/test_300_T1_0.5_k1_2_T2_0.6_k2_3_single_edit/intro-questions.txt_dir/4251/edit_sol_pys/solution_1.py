import itertools

def main():
    n = int(input())
    n_list = list(map(int, input().split()))
    print(solve(n, n_list))

def solve(n, n_list):
    combo = itertools.combinations(n_list, 3)
    combo = [sum(i) for i in combo]
    combo.sort()
    return combo[-3]

if __name__ == "__main__":
    main()
