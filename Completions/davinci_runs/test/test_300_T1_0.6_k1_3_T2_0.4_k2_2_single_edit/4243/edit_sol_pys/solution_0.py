

def main():
    A, B = map(int, input().split())
    if A >= 500:
        coins = (A // 500) * 1000 + (A % 500) // 5 * 5
    else:
        coins = A // 5 * 5
        
    print(coins)

if __name__ == '__main__':
    main()
