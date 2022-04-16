"""
You are organizing a Halloween party for your neighborhood. You are expecting many guests and want to provide them with costumes. You want to buy exactly one costume for each guest.
You are given the cost of each costume. You want to spend as little money as possible. However, you also want to provide a wide variety of costumes, so you want to buy a costume for each type (i.e., each different cost).
Write a program that computes the minimum amount of money you need to spend.
Input
The first line of the input contains a single integer n (1≤n≤100) — the number of costumes you are considering buying.
The second line of the input contains n integers c1,c2,…,cn (1≤ci≤100) — the costs of the costumes.
Output
Print a single integer — the minimum amount of money you need to spend.
"""

import sys

def main():
    n = int(input())
    costumes = dict()
    for i in range(n):
        costume = sys.stdin.readline().strip()
        if costume not in costumes:
            costumes[costume] = 1
        else:
            costumes[costume] += 1
    max_num = max(costumes.values())
    for costume in sorted(costumes):
        if costumes[costume] == max_num:
            print(costume)

if __name__ == "__main__":
    main()
