

import sys

def main():
    n = int(input())
    words = [input() for i in range(n)]
    count = {}
    for word in words:
        if word[0] in ["M", "A", "R", "C", "H"]:
            if word[0] in count:
                count[word[0]] += 1
            else:
                count[word[0]] = 1
    count_list = list(count.values())
    count_list.sort()
    print(count_list[0] * count_list[1] * count_list[2])

if __name__ == '__main__':
    main()