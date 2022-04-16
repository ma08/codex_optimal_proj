

cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib_list = [0,1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
