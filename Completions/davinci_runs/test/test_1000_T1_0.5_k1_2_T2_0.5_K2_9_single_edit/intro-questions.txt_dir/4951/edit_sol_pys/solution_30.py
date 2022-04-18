

def main():
    n = int(input())
    axioms = set()
    for i in range(n):
        assumptions, arrow, conclusion = input().split(' ')
        if assumptions == '':
            if conclusion not in axioms:
                print(i + 1)
                return
        else:
            for a in assumptions.split(' '):
                if a not in axioms:
                    print(i + 1)
                    return
    for a in axioms:
        print(a)
    print('correct')

if __name__ == '__main__':
    main()
