

def main():
    n, p, m = [int(x) for x in input().split()]
    names = [input() for i in range(n)]
    scores = {name: 0 for name in names}
    for _ in range(m):
        name, score = input().split()
        scores[name] += int(score)
    if all(score >= p for score in scores.values()):
        print("All winners")
    else:
        print("No winner")

if __name__ == '__main__':
    main()
