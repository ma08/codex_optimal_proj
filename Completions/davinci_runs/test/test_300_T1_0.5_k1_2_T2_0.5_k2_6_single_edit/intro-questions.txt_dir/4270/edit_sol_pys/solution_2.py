

def main():
    num_numbers = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    while len(numbers) > 1:
        numbers[0] = (numbers[0] + numbers[1]) / 2
        numbers.pop(1)
        numbers.sort()

    print(numbers[0])

if __name__ == '__main__':
    main()
