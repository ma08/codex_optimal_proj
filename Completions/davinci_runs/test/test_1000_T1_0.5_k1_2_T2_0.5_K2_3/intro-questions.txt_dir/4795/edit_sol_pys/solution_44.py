def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
list_of_values = input().split()


result = 0
for i in list_of_values:
    for j in range(1, len(i)):
        if int(i[j]) != 0:
            result += int(i[:j]) ** int(i[j])
            break
print(result)
