

def find_max(a):
    max_value = a[0]
    for i in a:
        if i > max_value:
            max_value = i
    return max_value
        
def find_min(a):
    min_value = a[0]
    for i in a:
        if i < min_value:
            min_value = i
    return min_value

def find_second_max(a):
    max_value = find_max(a)
    second_max_value = a[0]
    for i in a:
        if i > second_max_value and i != max_value:
            second_max_value = i
    return second_max_value


def find_second_min(a):
    min_value = find_min(a)
    second_min_value = a[0]
    for i in a:
        if i < second_min_value and i != min_value:
            second_min_value = i
    return second_min_value

def find_sum(a):
    sum = 0
    for i in a:
        sum += i
    return sum

def find_average(a):
    sum = find_sum(a)
    return sum/len(a)

def find_median(a):
    a.sort()
    if len(a) % 2 == 0:
        return (a[len(a) // 2] + a[len(a) // 2 - 1]) / 2
    else:
        return a[len(a) // 2]

def find_mode(a):
    a.sort()
    max_count = 0
    max_value = 0
    count = 0
    for i in a:
        if i == a[0]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_value = a[0]
            count = 1
            a[0] = i
    if count > max_count:
        max_count = count
        max_value = a[0]
    return max_value

def find_range(a):
    return find_max(a) - find_min(a)

def find_variance(a):
    average = find_average(a)
    sum = 0
    for i in a:
        sum += (i - average) ** 2
    return sum / len(a)

def find_standard_deviation(a):
    return find_variance(a) ** 0.5

def find_percentile(a, p):
    a.sort()
    return a[int(len(a) * p / 100)]

def find_first_quartile(a):
    return find_percentile(a, 25)

def find_third_quartile(a):
    return find_percentile(a, 75)

def find_interquartile_range(a):
    return find_third_quartile(a) - find_first_quartile(a)

n = int(input("Enter n: "))
a = list(map(int, input("Enter the elements of the list: ").split()))

print("Max:", find_max(a))
print("Min:", find_min(a))
print("Second Max:", find_second_max(a))
print("Second Min:", find_second_min(a))
print("Sum:", find_sum(a))
print("Average:", find_average(a))
print("Median:", find_median(a))
print("Mode:", find_mode(a))
print("Range:", find_range(a))
print("Variance:", find_variance(a))
print("Standard Deviation:", find_standard_deviation(a))
print("First Quartile:", find_first_quartile(a))
print("Third Quartile:", find_third_quartile(a))
print("Interquartile Range:", find_interquartile_range(a))
