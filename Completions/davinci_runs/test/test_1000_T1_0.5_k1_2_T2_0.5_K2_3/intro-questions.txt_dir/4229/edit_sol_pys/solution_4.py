

n = int(input())

# 1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17,Fizz,19,Buzz,Fizz,22,23,Fizz,Buzz,26,Fizz,28,29,FizzBuzz,31,32,Fizz,34,Buzz,Fizz,37,38,Fizz,Buzz,41,Fizz,43,44,FizzBuzz,46,47,Fizz,49,Buzz,Fizz,52,53,Fizz,Buzz,56,Fizz,58,59,FizzBuzz,61,62,Fizz,64,Buzz,Fizz,67,68,Fizz,Buzz,71,Fizz,73,74,FizzBuzz,76,77,Fizz,79,Buzz,Fizz,82,83,Fizz,Buzz,86,Fizz,88,89,FizzBuzz,91,92,Fizz,94,Buzz,Fizz,97,98,Fizz,Buzz

cnt = [0,0,0,0]
for i in range(1,n+1):
    if i % 15 == 0: cnt[3] += 1
    elif i % 3 == 0: cnt[2] += 1
    elif i % 5 == 0: cnt[1] += 1
    else: cnt[0] += 1

result = cnt[0] * (n-1)
result += cnt[1] * (n-5)
result += cnt[2] * (n-2)
result += cnt[3] * (n-15)

print(result)
