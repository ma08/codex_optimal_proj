

def main():
    n = int(input())
    axioms = []
    for i in range(n):
        assumptions, arrow, conclusion = input().split()
        if assumptions == '':
            axioms.append(conclusion)
        else:
            for a in assumptions.split():
                if a not in axioms:
                    print(i + 1)
                    return
            axioms.append(conclusion)
    print('correct')

if __name__ == '__main__':
    main()
