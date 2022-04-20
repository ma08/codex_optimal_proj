

n = int(input())

fizz_sum = 3 * (n//3) * (n//3 + 1) // 2
buzz_sum = 5 * (n//5) * (n//5 + 1) // 2
fizzbuzz_sum = 15 * (n//15) * (n//15 + 1) // 2

print(fizz_sum + buzz_sum - fizzbuzz_sum)