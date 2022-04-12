
def factorial(num):
    if num == 0:
        return 1 
    return num * factorial(num-1)

for _ in range(int(input())): 
    print(factorial(int(input())) % 10) 
