
import file
import sys

def main():
    num_pairs, num_days = map(int, sys.stdin.readline().strip().split())
    pairs = {}
    for _ in range(num_pairs):
        pair = sys.stdin.readline().strip()
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1
    if len(pairs) == num_pairs:
        print(num_days)
    else:
        print("paradox avoided")
