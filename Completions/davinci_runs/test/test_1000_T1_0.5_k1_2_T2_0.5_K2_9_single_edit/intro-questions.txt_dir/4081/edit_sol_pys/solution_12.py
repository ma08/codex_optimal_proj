

# SOLUTION

def problem_C2():
    num_of_cars = int(input())
    cars = list(map(int, input().split()))
    max_car = max(cars)
    d = [0] * (max_car + 1)

    # count the number of cars with the same length
    # d[i] = number of cars with length i
    for car in cars:
        d[car] += 1

    # d[0] = 1
    # d[-1] = 1
    d[0] = 1
    d[-1] = 1

    # p[i] = number of cars with length <= i
    p = [0] * (max_car + 1)
    for i in range(1, max_car + 1):
        p[i] = p[i - 1] + d[i]

    result = []

    # find the first car with length >= current car
    def find_first_car_with_length_greater_than_or_equal_to(x):
        if x == 0:
            return 0
        if x == p[max_car]:
            return max_car

        # find x in p using binary search
        l, r = 0, max_car
        while l < r:
            mid = (l + r) // 2
            if p[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l

    current_car_length = 0
    for i in range(num_of_cars):
        if cars[i] > current_car_length:
            result.append('R')
            current_car_length = cars[i]
        else:
            x = find_first_car_with_length_greater_than_or_equal_to(p[current_car_length] - i)
            if x > current_car_length:
                result.append('R')
                current_car_length = x
            else:
                result.append('L')

    print(len(result))
    print(''.join(result))


problem_C2()
