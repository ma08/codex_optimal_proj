
n = int(input())

fizz = n // 3
buzz = n // 5
fizzbuzz = n // 15
print(3 * fizz * (fizz + 1) // 2 + 5 * buzz * (buzz + 1) // 2 - 15 * fizzbuzz * (fizzbuzz + 1) // 2)
