"""
Solution:


"""

def run():
    n = int(input())

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    print(factorial(n) // (factorial(n // 2) ** 2))


if __name__ == "__main__":
    run()
