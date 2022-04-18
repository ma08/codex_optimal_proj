

def main():
    n = int(input())
    assumptions = set()
    for i in range(n):
        a, arrow, c = input().split()
        if a == '':
            assumptions.add(c)
        else:
            for a_ in a.split():
                if a_ not in assumptions:
                    print(i + 1)
                    return
            assumptions.add(c)
    print('correct')

if __name__ == '__main__':
    main()
