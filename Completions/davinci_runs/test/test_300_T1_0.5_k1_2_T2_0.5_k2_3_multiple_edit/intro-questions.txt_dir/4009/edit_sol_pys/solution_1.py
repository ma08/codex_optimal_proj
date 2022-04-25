

def solve(n, x, y, number_list):
    operations = 0
    for i in range(n-x+1):
        if number_list[i] != number_list[i+x-y]:
            operations += 1
    return operations

def main():
    n, x, y = map(int, input().split()) # n = length of string, x = length of substring, y = length of substring
    number_list = input()
    print(solve(n, x, y, number_list))

if __name__ == "__main__":
    main()
