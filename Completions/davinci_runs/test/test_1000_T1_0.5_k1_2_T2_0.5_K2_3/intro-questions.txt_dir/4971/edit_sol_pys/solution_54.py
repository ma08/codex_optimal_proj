
from random import shuffle

def main():
    n = int(input())
    random_list = [i for i in range(1, n+1)]
    shuffle(random_list)
    random_list.sort()
    return random_list

print(main())
