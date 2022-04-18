
# while loop
n = int(input())

while True:
    n += 1
    if n % sum([int(i) for i in str(n)]) == 0:
        print(n)
        break

# fix syntax errors
def main():
    n = int(input())
    if n == 0:
        print(0)
    else:
        print(n + sum(range(1, n)))

if __name__ == '__main__':
    main()
