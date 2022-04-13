
def main():
    n = int(input())
    assumptions = set()
    for i in range(n):
        left, arrow, right = input().split(' ')
        if left == '':
            assumptions.add(right)
        else:
            for a in left.split(' '):
                if a not in assumptions:
                    print(i + 1)
                    return
            assumptions.add(right)
    print('correct')

if __name__ == '__main__':
    main()
