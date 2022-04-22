def fizz_buzz(n):
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)



n, k = map(int, input().split())
s = input()

# if k > n or k == 0:
#     print(-1)
# else:
#     print(n - k)

if k > n or k == 0:
    print(-1)
else:
    print(n - k)
