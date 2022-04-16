
def solve(x):
    x_str = str(x)
    num_digits = len(x_str)
    if num_digits == 1:
        return x
    num_presses = 0
    for i in range(1, num_digits):
        num_presses += (9*(10**(i-1)))*i


    num_presses += (num_digits-1)*(x - 10**(num_digits-1))
    num_presses += num_digits*(10**(num_digits-1))
    return num_presses


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x = int(input())
        print(solve(x))
