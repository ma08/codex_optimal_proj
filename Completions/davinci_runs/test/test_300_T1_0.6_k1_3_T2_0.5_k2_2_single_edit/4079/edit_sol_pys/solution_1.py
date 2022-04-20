

def main():
    n = int(input())
    for i in range(n):
        test = input()
        if len(test) != len(set(test)) or ord(test[-1]) - ord(test[0]) != len(test)-1:
            print('No')
        else:
            print('Yes')


if __name__ == "__main__":
    main()
