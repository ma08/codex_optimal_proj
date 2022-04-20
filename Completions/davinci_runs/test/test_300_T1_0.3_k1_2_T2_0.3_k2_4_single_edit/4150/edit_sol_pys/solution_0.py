

n, k = map(int, input().split())
a = list(map(int, input().split()))

# print(n, k)
# print(a)

# 1. find the max
# 2. find the k closest to the left and right of the max
# 3. remove the max and the k closest left and right
# 4. repeat

# 1. find the max
def find_max(a):
    max_index = 0
    max_value = a[0]
    for i in range(1, len(a)):
        if a[i] > max_value:
            max_index = i
            max_value = a[i]
    return max_index

# 2. find the k closest to the left and right of the max
def find_k_closest(a, max_index, k):
    left_index = max_index - 1
    right_index = max_index + 1
    left_count = 0
    right_count = 0
    while left_count < k and left_index >= 0:
        left_count += 1
        left_index -= 1
    while right_count < k and right_index < len(a):
        right_count += 1
        right_index += 1
    return left_index + 1, right_index - 1

# 3. remove the max and the k closest left and right
def remove_max_and_k_closest(a, max_index, left_index, right_index):
    a = a[:left_index] + a[right_index+1:]
    return a

# 4. repeat
def repeat(a, k):
    result = []
    while len(a) > 0:
        max_index = find_max(a)
        left_index, right_index = find_k_closest(a, max_index, k)
        a = remove_max_and_k_closest(a, max_index, left_index, right_index)
        result += [left_index, right_index]
    return result

# 5. print the result
def print_result(result, n):
    result_string = ""
    for i in range(n):
        if i in result:
            result_string += "1"
        else:
            result_string += "2"
    print(result_string)

def main():
    result = repeat(a, k)
    print_result(result, n)

if __name__ == "__main__":
    main()
