

def median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        med = (lst[len(lst)//2] + lst[len(lst)//2 - 1])/2
    else: med = lst[len(lst)//2]
    return(med)

def main():
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))[:n]
    c = 0
    for i in range(n):
        for j in range(i, n+1):
            if median(seq[i:j]) == m:
                c += 1
    print(c)

if __name__ == '__main__':
    main()
