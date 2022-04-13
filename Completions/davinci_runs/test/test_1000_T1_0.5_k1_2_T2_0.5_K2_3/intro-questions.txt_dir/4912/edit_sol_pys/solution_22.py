
def main(n):
    for i in range(1, n+1):
        if n%i == 0:
            print(i, end=" ")
if __name__ == '__main__':
    n = int(input())
    main(n)
