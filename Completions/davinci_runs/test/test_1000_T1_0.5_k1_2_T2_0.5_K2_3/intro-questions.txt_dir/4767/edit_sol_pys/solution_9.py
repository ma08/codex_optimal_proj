
import sys

def main():
    vals = [int(x) for x in input().split()]
    out = 0
    for i in range(7, -1, -1):
        out += 19 - vals[i]
    print(out)

main()
