
def fibonacci(n):
    fib_list = [0,1]
    for i in range(2,n):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list[0:n]
cube = lambda x: x**3


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n)))) 
