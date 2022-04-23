

def solve(n, lengths):
    return "Yes" if (max(lengths) < sum(lengths) - max(lengths)) else "No"

def main():
    n = int(input())
    lengths = list(map(int, input().split())) 

    print(solve(n, lengths))

if __name__ == '__main__':
    main()
