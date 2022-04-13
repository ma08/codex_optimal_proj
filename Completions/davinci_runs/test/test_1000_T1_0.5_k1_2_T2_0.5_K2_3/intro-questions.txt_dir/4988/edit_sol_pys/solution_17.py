
def last_digit(n):
    if n < 10:
        return n

    n_string = str(n)
    length = len(n_string)
    last_digit = n_string[length-1]
    second_last_digit = n_string[length-2]
    first_part = n_string[0:length-2]

    return int(first_part) ** int(second_last_digit) % 10

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        n = input().strip()
        print(last_digit(int(n)))

if __name__ == '__main__':
    main()
