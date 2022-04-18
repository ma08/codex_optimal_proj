from math import ceil

def find_floor(n, x, floors=1):
    if n == 0: return floors
    if n <= x: return floors + 1
    return find_floor(n - x, x, floors + 1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split()) 
        print(find_floor(n, x))
