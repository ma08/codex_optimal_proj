

def divisible_by_three(s):
    return sum(int(digit) for digit in s) % 3 == 0

def max_divisible(s):
    if divisible_by_three(s):
        return len(s) - 1
    else:
        return len(s)

if __name__ == '__main__':
    s = input()
    print(max_divisible(s))