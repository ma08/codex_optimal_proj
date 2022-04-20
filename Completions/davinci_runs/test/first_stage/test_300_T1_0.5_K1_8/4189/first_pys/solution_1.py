


def solve(cheeses):
    soft_cheeses = []
    hard_cheeses = []
    for cheese in cheeses:
        if cheese[1] == 'soft':
            soft_cheeses.append(cheese[0])
        elif cheese[1] == 'hard':
            hard_cheeses.append(cheese[0])

    soft_cheeses.sort()
    hard_cheeses.sort()

    if len(hard_cheeses) > len(soft_cheeses):
        return len(hard_cheeses)
    else:
        return len(soft_cheeses)

if __name__ == '__main__':
    n = int(input())
    cheeses = []
    for _ in range(n):
        cheeses.append(input().split())
    print(solve(cheeses))