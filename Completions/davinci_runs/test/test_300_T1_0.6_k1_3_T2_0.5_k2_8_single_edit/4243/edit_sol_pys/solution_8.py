

def main():
    a = int(input())
    if a >= 500:
        coins = (a // 500) * 1000 + (a % 500) // 5 * 5
    else:
        coins = a // 5 * 5
        
    print(coins)

if __name__ == '__main__':
    main()
