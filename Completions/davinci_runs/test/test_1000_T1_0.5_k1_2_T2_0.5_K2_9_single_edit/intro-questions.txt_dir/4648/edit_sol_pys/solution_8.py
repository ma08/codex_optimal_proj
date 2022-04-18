

def is_even(n):
    return n % 2 == 0

def is_divisible_by_3(n):
    return n % 3 == 0

def is_divisible_by_4(n):
    return n % 4 == 0

def is_divisible_by_5(n):
    return n % 5 == 0

def is_divisible_by_6(n):
    return n % 6 == 0

def is_divisible_by_8(n):
    return n % 8 == 0

def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        moves = 0
        if n == 1:
            print(0)
            continue
        elif is_divisible_by_6(n):
            n /= 6
            moves += 1
        elif is_divisible_by_3(n):
            n *= 2
            moves += 1
        elif is_even(n):
            n /= 2
            moves += 1
        elif is_divisible_by_5(n):
            n *= 4
            moves += 2
        elif is_divisible_by_4(n):
            n *= 3
            moves += 2
        elif is_divisible_by_8(n):
            n *= 5
            moves += 3
        else:
            print(-1)
            continue

        print(moves)

if __name__ == "__main__":
    main()
