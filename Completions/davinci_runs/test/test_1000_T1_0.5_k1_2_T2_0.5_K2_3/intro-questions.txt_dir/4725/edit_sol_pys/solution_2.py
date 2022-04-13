
import sys

def main():
    for line in sys.stdin:
        res = 0
        count = [0]*26  # to count the number of each alphabet
        for i in line:
            count[ord(i)-ord('a')] += 1  # ord() return the ascii code of i, ord('a') return the ascii code of 'a'
        for i in count:
            if i > 2:
                res += i-2  # count the number of alphabets that occur more than twice
        print(res)


main()
