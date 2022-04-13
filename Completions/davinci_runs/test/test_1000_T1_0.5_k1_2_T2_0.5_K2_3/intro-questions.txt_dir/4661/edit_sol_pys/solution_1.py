

cube = lambda x: x**3

def fibonacci(n):
    a = 0
    b = 1
    c = 0
    result = [a, b]
    for i in range(n):
        c = a + b 
        result.append(c)
        a = b
        b = c
    return result

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
