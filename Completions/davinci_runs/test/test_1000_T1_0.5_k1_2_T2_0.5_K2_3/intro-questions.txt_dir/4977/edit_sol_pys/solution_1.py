
def main():
    n = int(input())
    for i in range(n):
        charge = int(input())
        start = [int(x) for x in input().split()]
        end = [int(x) for x in input().split()]
        if abs(start[0] - end[0]) + abs(start[1] - end[1]) == charge:
            print('Y')
        else:
            print('N')


main()
