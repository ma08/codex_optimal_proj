

def main():
    n = int(input())
    axioms = set()
    for i in range(n):
        assumptions, arrow, conclusion = input().split(' ')
        if assumptions == '':
            axioms.add(conclusion)
        else:
            for a in assumptions.split(' '):
                if a not in axioms:
                    print(i + 1)
                    return
            axioms.add(conclusion)
    print('correct')

if __name__ == '__main__':
    main()