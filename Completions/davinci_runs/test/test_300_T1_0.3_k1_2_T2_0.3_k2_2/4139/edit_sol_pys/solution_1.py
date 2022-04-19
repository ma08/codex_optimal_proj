

def main():
    n = int(input())
    print(sum(1 for i in range(1, n+1) if '7' in str(i) and '5' in str(i) and '3' in str(i)))

if __name__ == '__main__':
    main()
