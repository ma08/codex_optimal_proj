def solve(N, V):
    V.sort()
    while len(V) > 1:
        a = V.pop(0)
        b = V.pop(0)
        V.append((a + b) / 2)
        V.sort()
    return V[0]

if __name__ == "__main__":
    N = int(input())
    V = [int(x) for x in input().split()]
    print(solve(N, V))
