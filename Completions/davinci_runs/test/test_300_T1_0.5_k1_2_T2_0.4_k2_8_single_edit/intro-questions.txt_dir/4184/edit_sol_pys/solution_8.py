

def get_input():
    number = int(input())
    return number

def get_input_list():
    numbers = list(map(int, input().split()))
    return numbers

def get_max_diff(numbers):
    numbers.sort()
    return numbers[-1] - numbers[0]

def get_min_diff(numbers):
    numbers.sort()
    return numbers[1] - numbers[0]

def get_max_min_diff(numbers):
    max_diff = get_max_diff(numbers)
    min_diff = get_min_diff(numbers)
    return max_diff, min_diff

def main():
    number = get_input()
    numbers = get_input_list()
    max_diff, min_diff = get_max_min_diff(numbers)
    print(max_diff, min_diff)

if __name__ == "__main__":
    main()
