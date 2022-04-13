

def main():
    n = int(input())
    assumptions = set()
    for i in range(n):
        a, arrow, c = input().split(' ')
        if a == '':
            assumptions.add(c)
        else:
            for axiom in a.split(' '):
                if axiom not in assumptions:
                    print(i + 1)
                else:
                    assumptions.remove(axiom)
                    return
            assumptions.add(c)
    print('correct')

if __name__ == '__main__':
    main()
