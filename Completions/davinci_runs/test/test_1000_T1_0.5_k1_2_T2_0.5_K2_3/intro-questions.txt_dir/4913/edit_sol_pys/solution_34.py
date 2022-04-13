#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline().strip())
    vac = [0, 0, 0]
    ctrl = [0, 0, 0]
    for i in range(n):
        line = sys.stdin.readline().strip()
        if line[0] == 'Y':
            for j in range(3):
                if line[j+1] == 'Y':
                    vac[j] += 1
        else:
            for j in range(3):
                if line[j+1] == 'Y':
                    ctrl[j] += 1
    for i in range(3):
        if ctrl[i] == 0:
            print("Not effective")
        else:
            print("{:.6f}".format((vac[i]/ctrl[i])*100))

if __name__ == "__main__":
    main()
