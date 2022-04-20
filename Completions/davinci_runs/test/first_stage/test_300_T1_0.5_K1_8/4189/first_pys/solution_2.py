

def main():
    cheeses = []
    num_cheeses = int(input())
    for i in range(num_cheeses):
        name, type = input().split()
        cheeses.append((name, type))

    soft_count = 0
    hard_count = 0
    for cheese in cheeses:
        if cheese[1] == 'soft':
            soft_count += 1
        elif cheese[1] == 'hard':
            hard_count += 1

    print(min(soft_count, hard_count))

if __name__ == "__main__":
    main()