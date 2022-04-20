

n = int(input())

# 1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
# 1,2,0,4,0,0,7,8,0,0,11,0,13,14,0,16,0,0,19,0

cnt = [0,0,0,0,0]
for i in range(n):
    if i % 15 == 0:
        cnt[3] += 1
    elif i % 3 == 0:
        cnt[2] += 1
    elif i % 5 == 0:
        cnt[1] += 1
    else:
        cnt[0] += 1

print(cnt)

result = 0
result += cnt[0] * (n-1)
result += cnt[1] * (n-5)
result += cnt[2] * (n-2)
result += cnt[3] * (n-15)

print(result)
