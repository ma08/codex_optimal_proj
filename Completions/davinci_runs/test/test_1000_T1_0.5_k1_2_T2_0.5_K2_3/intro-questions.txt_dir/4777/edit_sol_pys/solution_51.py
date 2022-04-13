

def main():
    k = int(input())
    a, b = 1, 1
    for _ in range(k-1):
        a, b = b, a+b # the last one is the (k+1)-th fibonacci number
    print(a, b) # the k-th fibonacci number and the (k+1)-th fibonacci number

if __name__ == "__main__":
    main()
