
from itertools import combinations

def main():
    s = input()
    for c in combinations(range(len(s) - 1), i):
        tmp = s
        for j in c:
            tmp = tmp[:j+1] + '+' + tmp[j+1:]
        print(tmp, sum(map(int, tmp.split('+'))))

if __name__ == '__main__':
    main()
