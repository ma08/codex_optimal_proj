
import sys

def main():
    vals = [int(x) for x in sys.stdin.readline().split()][:8]
    out = 0
    for i in range(7, -1, -1):
        out += 19 - vals[i]
    print(out)

main()
