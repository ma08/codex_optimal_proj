
import sys

def main():
    n = int(sys.stdin.readline())
    counter = 0
    for i in range(n):
        word = sys.stdin.readline()
        if "pink" in word.lower() or "rose" in word.lower():
            counter += 1
    if counter == 0:
        print("I must watch Star Wars with my daughter")
    else:
        print(counter)

if __name__ == '__main__':
    main()
