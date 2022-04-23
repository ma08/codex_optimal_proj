

def main():
    x, n = map(int, input().split()) # x: number, n: length of list
    p = sorted(list(map(int, input().split()))) # p: list of numbers

    if x < p[0]: # x is smaller than the smallest number in p
        print(p[0] - x) 
    elif x > p[-1]: # x is bigger than the biggest number in p
        print(x - p[-1]) 
    else:
        for i in range(n-1): 
            if x < p[i+1]: # x is smaller than the next number in p
                print(min(x-p[i], p[i+1] - x)) # print the smaller distance
                break

if __name__ == '__main__':
    main()
