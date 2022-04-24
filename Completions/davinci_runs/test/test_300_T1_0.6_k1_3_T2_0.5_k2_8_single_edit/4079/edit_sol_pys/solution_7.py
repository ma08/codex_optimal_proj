

def main():
    n = int(input())
    for i in range(n):
        test = input()
        if len(test) != len(set(test)): # checks if there is duplicate characters
            print('No')
        elif ord(test[-1]) - ord(test[0]) != len(test)-1: # checks if the word is in order
            print('No')
        else:
            print('Yes')


if __name__ == "__main__":
    main()
