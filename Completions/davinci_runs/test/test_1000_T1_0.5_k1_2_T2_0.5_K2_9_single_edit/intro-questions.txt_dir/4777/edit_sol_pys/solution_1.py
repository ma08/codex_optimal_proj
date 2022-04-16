

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        if i == 0:
            b = 1
        elif i == 1:
            b = 1
            a = 1
        else:
            temp = b
            b = a + b
            a = temp

    print(a, b)


if __name__ == "__main__":
    k = int(input())
    fibonacci(k)
