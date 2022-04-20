

import random

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort(reverse=True)
    while len(a_list) > 1:
        i = random.randint(0, len(a_list)-1)
        j = random.randint(0, len(a_list)-1)
        while i == j:
            j = random.randint(0, len(a_list)-1)
        a_list[i] -= a_list[j]
        if a_list[i] <= 0:
            a_list.pop(i)
            if i < j:
                j -= 1
        a_list.pop(j)
    print(a_list[0])

if __name__ == '__main__':
    main()