

def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        moves = 0
        while n > 1:
            if n % 6 == 0:
                n = n // 6
                moves += 1
            else:
                n *= 2
                moves += 1
        print(moves)

if __name__ == "__main__":
    main()
