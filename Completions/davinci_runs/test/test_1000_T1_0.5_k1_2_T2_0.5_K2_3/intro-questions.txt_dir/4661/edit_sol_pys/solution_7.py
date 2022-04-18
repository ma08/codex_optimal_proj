cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a, b = 0, 1
    for i in range(n):       
        a, b = b, a + b
    return a

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
