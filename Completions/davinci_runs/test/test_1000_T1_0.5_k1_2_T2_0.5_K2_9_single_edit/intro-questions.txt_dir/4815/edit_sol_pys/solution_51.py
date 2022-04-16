from collections import defaultdict


def main():
    n, m = [int(x) for x in input().split()]
    names = [input() for _ in range(n)] #['abc', 'def', 'ghi']
    scores = {name:0 for name in names} #{'abc':0, 'def':0, 'ghi':0}
    for _ in range(m): #m = 2
        name, score = input().split() #'abc', '5'
        scores[name] += int(score) #{'abc':5, 'def':0, 'ghi':0}
        if scores[name] >= 100:
            print(name, "wins!") #abc wins!
            return #return from the function
    print("No winner!") #No winner!

if __name__ == '__main__':
    main()
