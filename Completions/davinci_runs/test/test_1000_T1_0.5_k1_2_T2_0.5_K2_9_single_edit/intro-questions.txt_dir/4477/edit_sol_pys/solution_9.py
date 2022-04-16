
def solve(x):
    x_str = str(x)
    first_digit = int(x_str[0])
    num_digits = len(x_str)
    num_presses = x
    for i in range(1, num_digits):
        num_presses += i * (first_digit * (10 ** (i - 1)))
    return num_presses


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x = int(input())
        print(solve(x))
