

def solve(n, x, y, number_list, number_list2):
    operations = 0
    for i in range(n - x):
        if number_list[i] != number_list2[i + x - y]:
            operations += 1

    return operations

def main():
    n, x, y = map(int, input().split())
    number_list2 = input()
    number_list = input()
    print(solve(n, x, y, number_list))

if __name__ == "__main__":
    main()
