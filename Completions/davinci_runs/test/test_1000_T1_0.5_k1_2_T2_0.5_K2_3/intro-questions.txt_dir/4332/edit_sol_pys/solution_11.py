
def main():
    n = int(input())
    number = [int(i) for i in str(n)]
    if n % sum(number) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__': main()
