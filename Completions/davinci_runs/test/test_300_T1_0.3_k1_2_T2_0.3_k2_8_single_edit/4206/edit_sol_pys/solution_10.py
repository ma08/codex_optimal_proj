

def is_divisible_by_three(number):
    return number % 3 == 0

def get_number_of_divisible_by_three(number):
    number_of_divisible_by_three = 0
    for digit in number:
        if is_divisible_by_three(int(digit)):
            number_of_divisible_by_three += 1
    return number_of_divisible_by_three

def get_max_number_of_divisible_by_three(number):
    max_number_of_divisible_by_three = 0
    for i in range(len(number)):
        if i == 0:
            max_number_of_divisible_by_three = get_number_of_divisible_by_three(number[:i])
        else:
            max_number_of_divisible_by_three = max(max_number_of_divisible_by_three, get_number_of_divisible_by_three(number[:i]))
    return max_number_of_divisible_by_three

def main():
    number = input()
    print(get_max_number_of_divisible_by_three(number))

if __name__ == '__main__':
    main()
