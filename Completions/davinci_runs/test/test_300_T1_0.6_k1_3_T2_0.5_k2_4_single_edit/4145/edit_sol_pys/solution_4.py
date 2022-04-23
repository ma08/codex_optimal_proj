
def find_minimum_prime(n):
    for i in range(n, n + 100):
        if all(i % j != 0 for j in range(2, i)):
            return i

if __name__ == '__main__':
    x = int(input())
    print(find_minimum_prime(x))
