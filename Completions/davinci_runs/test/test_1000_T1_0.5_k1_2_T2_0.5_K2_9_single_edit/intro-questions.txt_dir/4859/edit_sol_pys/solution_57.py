
import sys

def main():
    b, d, c, l = map(int, sys.stdin.readline().split())
    if l % 2 == 1 or l < b or l < c or l < d or l > b + d + c * 2:
        print("impossible")
        return
    for i in range(0, l // b + 1):
        for j in range(0, l // d + 1):
            for k in range(0, l // c + 1):
                if i * b + j * d + k * c == l:
                    print(i, j, k)

main()
