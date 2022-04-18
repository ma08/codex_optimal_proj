

import sys
 
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')
 
f = sys.stdin
o = sys.stdout
 
def solve(a, b, c, k):
    if a + b + c > k:
        return None
    if a + b + c == k:
        return [a, b, c]
    for i in range(k // a + 1):
        for j in range(k // b + 1):
            for l in range(k // c + 1):
                if i * a + j * b + l * c == k:
                    return [i, j, l]
    return None
 
def main():
    b, d, c, l = map(int, f.readline().split())
    solutions = []
    for i in range(l // b + 1):
        for j in range(l // d + 1):
            for k in range(l // c + 1):
                if i * b + j * d + k * c == l:
                    solutions.append([i, j, k])
    if len(solutions) == 0:
        print("impossible", file = o)
    else:
        for i in sorted(solutions):
            print(*i, file = o)
 
if __name__ == "__main__":
    main()
