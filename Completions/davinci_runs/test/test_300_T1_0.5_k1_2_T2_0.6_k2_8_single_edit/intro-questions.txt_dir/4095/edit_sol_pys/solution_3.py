


def median(numbers):
    if len(numbers) % 2 == 0:
        med = numbers[len(numbers)//2] + numbers[len(numbers)//2 - 1]
    else:
        med = numbers[len(numbers)//2]
    return med


def main():
    n, m = map(int, input().split())  # number of numbers and the target number
    numbers = list(map(int, input().split()))  # the list of numbers
    counter = 0
    for i in range(n):  # iterate through the list
        for j in range(i, n):  # iterate through the sublist
            if median(numbers[i:j+1]) == m:  # check if the median of the sublist is equal to the target
                counter += 1
    print(counter)

if __name__ == '__main__':
    main()
