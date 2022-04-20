

def solve(n, x, y, number, operations):
    operations = 0
    for i in range(n):
        if number[i] != number[i+x]:
            operations += 1 
    return operations 


def main():
    n, x, y = map(int, input().split())
    number = input()
    operations = 0
    print(solve(n, x, y, number, operations))

if __name__ == "__main__":
    main()
