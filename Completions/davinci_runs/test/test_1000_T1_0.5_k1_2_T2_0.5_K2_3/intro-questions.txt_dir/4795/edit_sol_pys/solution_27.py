

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
list_of_values = [1, 2, 3, 4]


result = 0
for i in range(1, len(list_of_values)):
    if int(list_of_values[i]) != 0:
        result += int(list_of_values[:i]) ** int(list_of_values[i])
        break
print(result)
