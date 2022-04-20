

import sys

def main():
    input_list = sys.stdin.readlines()
    #input_list = ["15 2\n", "1 2 1 1 1 2 1 1 2 1 2 1 1 1 1\n"]
    #input_list = ["10 4\n", "1 3 1 3 10 3 7 7 12 3\n"]
    #input_list = ["7 3\n", "1 2 3 2 4 3 1\n"]
    input_list = [x.strip() for x in input_list]
    input_list = [[int(y) for y in x.split()] for x in input_list]
    print(input_list)
    #print(input_list)
    n = input_list[0][0]
    k = input_list[0][1]
    s = input_list[1]
    #print(n, k, s)
    #print(s)
    d = {}
    for i in s:
        if i in d: d[i] += 1
        else: d[i] = 1
    #print(d)
    d = sorted(d.items(), key = lambda x: x[1], reverse = True)
    #print(d)
    answer = [d[i][0] for i in range(k)]
    print(' '.join(str(x) for x in answer))

main()