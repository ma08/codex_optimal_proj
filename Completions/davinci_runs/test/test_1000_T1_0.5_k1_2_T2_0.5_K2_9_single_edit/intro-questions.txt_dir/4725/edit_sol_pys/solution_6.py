

import sys

def main():
    inp = sys.stdin.readline().strip()
    if len(inp) <= 2:
        print(0)
        return
    freq = {}
    for char in inp:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    if len(freq) <= 2:
        print(0)
        return
    else:
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        if freq[2][1] == 1:
            print(len(inp) - 2)
            return
        else:
            print(len(inp) - 1 - freq[1][1] - freq[2][1])

if __name__ == '__main__':
    main()
