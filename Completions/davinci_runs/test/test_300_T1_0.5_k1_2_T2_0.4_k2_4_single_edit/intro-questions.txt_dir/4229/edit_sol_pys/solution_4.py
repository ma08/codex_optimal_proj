


def fizzbuzz(n):
    if n % 15 == 0:
        return 3
    elif n % 3 == 0:
        return 2
    elif n % 5 == 0:
        return 1
    else:
        return 0

n = int(input())

# 1,2,\mbox{Fizz},4,\mbox{Buzz},\mbox{Fizz},7,8,\mbox{Fizz},\mbox{Buzz},11,\mbox{Fizz},13,14,\mbox{FizzBuzz},16,17,\mbox{Fizz},19,\mbox{Buzz},\mbox{Fizz},22,23,\mbox{Fizz},\mbox{Buzz},26,\mbox{Fizz},28,29,\mbox{FizzBuzz},31,32,\mbox{Fizz},34,\mbox{Buzz},\mbox{Fizz},37,38,\mbox{Fizz},\mbox{Buzz},41,\mbox{Fizz},43,44,\mbox{FizzBuzz},46,47,\mbox{Fizz},49,\mbox{Buzz},\mbox{Fizz},52,53,\mbox{Fizz},\mbox{Buzz},56,\mbox{Fizz},58,59,\mbox{FizzBuzz},61,62,\mbox{Fizz},64,\mbox{Buzz},\mbox{Fizz},67,68,\mbox{Fizz},\mbox{Buzz},71,\mbox{Fizz},73,74,\mbox{FizzBuzz},76,77,\mbox{Fizz},79,\mbox{Buzz},\mbox{Fizz},82,83,\mbox{Fizz},\mbox{Buzz},86,\mbox{Fizz},88,89,\mbox{FizzBuzz},91,92,\mbox{Fizz},94,\mbox{Buzz},\mbox{Fizz},97,98,\mbox{Fizz},\mbox{Buzz}
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100
# 1,2,0,4,0,0,7,8,0,0,11,0,13,14,0,16,0,0,19,0,0,22,0,0,0,26,0,28,0,0,31,32,0,34,0,0,37,38,0,0,41,0,43,44,0,46,0,0,49,0,0,52,0,0,0,56,0,58,0,0,61,62,0,64,0,0,67,68,0,0,71,0,73,74,0,76,0,0,79,0,0,82,0,0,0,86,0,88,0,0,91,92,0,94,0,0,97,98,0,0,101
# 1,2,0,4,0,0,7,8,0,0,11,0,13,14,0,16,0,0,19,0,0,22,0,0,0,26,0,28,0,0,31,32,0,34,0,0,37,38,0,0,41,0,43,44,0,46,0,0,49,0,0,52,0,0,0,56,0,58,0,0,61,62,0,64,0,0,67,68,0,0,71,0,73,74,0,76,0,0,79,0,0,82,0,0,0,86,0,88,0,0,91,92,0,94,0,0,97,98,0,0,101

cnt = [0,0,0,0,0]
for i in range(n):
    cnt[fizzbuzz(i)] += 1

# print(cnt)

result = 0
result += cnt[0] * (i+1)
result += cnt[1] * (i-4)
result += cnt[2] * (i-1)
result += cnt[3] * (i-14)

print(result)
