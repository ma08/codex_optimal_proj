

def is_divisible_by_three(n):
    return n % 3 == 0

def get_number_of_divisible_by_three(n):
    return len(list(filter(is_divisible_by_three, map(int, n))))

def get_max_number_of_divisible_by_three(n):
    return max(map(get_number_of_divisible_by_three, [n[i:] for i in range(len(n))]))

def main():
    n = input()
    print(get_max_number_of_divisible_by_three(n))

if __name__ == '__main__':
    main()
