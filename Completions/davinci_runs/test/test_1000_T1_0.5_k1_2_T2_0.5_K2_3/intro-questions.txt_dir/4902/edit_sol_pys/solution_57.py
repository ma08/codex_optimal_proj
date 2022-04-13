import sys

def main():
    word = sys.stdin.readline().strip()
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    # print(counter)
    odd = []
    for value in counter.values():
        if value % 2 != 0:
            odd.append(value)
    print(len(odd) - 1)

if __name__ == '__main__':
    main()
