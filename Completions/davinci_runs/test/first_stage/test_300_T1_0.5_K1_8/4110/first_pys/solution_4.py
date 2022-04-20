

import sys

def main():
    D, G = map(int, sys.stdin.readline().split())
    p_c_list = []
    for i in range(D):
        p, c = map(int, sys.stdin.readline().split())
        p_c_list.append([p, c])
    p_c_list.reverse()
    result = 0
    total_score = 0
    while total_score < G:
        if len(p_c_list) == 0:
            result += 1
            total_score += 100 * (D + 1)
        else:
            p, c = p_c_list.pop()
            if total_score + p * 100 * (D + 1) + c >= G:
                result += (G - total_score - 1) // (100 * (D + 1)) + 1
                total_score = G
            else:
                result += p
                total_score += p * 100 * (D + 1) + c
    print(result)

main()