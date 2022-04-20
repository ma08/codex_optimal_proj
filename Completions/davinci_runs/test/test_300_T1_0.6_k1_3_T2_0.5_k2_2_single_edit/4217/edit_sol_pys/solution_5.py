

import sys

def main():
    N, M = map(int, input().split())
    dic = dict.fromkeys(range(1, M+1), 0) # create dictionary with key 1~M, value 0
    for i in range(N):
        for j in map(int, sys.stdin.readline().split()[1:]):
            dic[j] += 1 # count the number of people who like the hobby
    print(sum([1 for e in dic.values() if e == N])) # print the number of the hobby that everyone liked

if __name__ == '__main__':
    main()
