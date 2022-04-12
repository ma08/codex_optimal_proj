
import sys

def main():
    a, b = sys.stdin.readline().strip().split()
    for i in range(len(b)):  # for each word in b
        if b[i] in a:  # if the word is in a
            for j in range(i):
                print('.' * len(a))  # print the word with dots
            print(a)  # print the word
            for j in range(i+1, len(b)):
                print('.' * len(a))  # print the word with dots
            break  # break the loop

if __name__ == "__main__":
    main()
