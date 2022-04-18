

import collections

def main():
    hand = input().split() #hand is a list of strings
    strength = max(collections.Counter(hand).values()) #Counter() is a class that counts the number of occurences of each element in a list
    print(strength)

if __name__ == "__main__":
    main()
