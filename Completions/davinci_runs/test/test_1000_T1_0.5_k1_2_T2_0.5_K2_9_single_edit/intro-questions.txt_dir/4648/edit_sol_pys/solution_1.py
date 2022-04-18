

def is_power_of_6(n):
    while n > 1:
        if n % 6 == 0:
            n /= 6
        else:
            return False
    return True

def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        moves = 0
        if n == 1:
            print(0)
        else:
            while not is_power_of_6(n):
                n *= 2
                moves += 1
            print(moves)

if __name__ == "__main__":
    main()
