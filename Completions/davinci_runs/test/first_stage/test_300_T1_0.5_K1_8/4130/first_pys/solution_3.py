

def main():
    n = int(input())
    ai = list(map(int, input().split()))
    weights = set()
    for i in range(n):
        if ai[i] - 1 in weights:
            weights.add(ai[i] - 1)
        elif ai[i] + 1 in weights:
            weights.add(ai[i] + 1)
        else:
            weights.add(ai[i])
    print(len(weights))

if __name__ == "__main__":
    main()