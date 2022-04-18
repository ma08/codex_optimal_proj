
# https://codeforces.com/contest/1154/problem/A
# https://codeforces.com/contest/1154/submission/65212073

def main():
    # get input
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    # get max
    max_a = max(a)
    max_b = max(b)
    
    # get other elements
    a.remove(max_a)
    b.remove(max_b)
    
    # print result (max_a * max_b) - (a[0] * b[1])
    print(max_a * max_b - a[0] * b[1], end = " ")
    
    # get min
    min_a = min(a)
    min_b = min(b)
    
    # print result (max_a * min_b) - (a[0] * b[0])
    print(max_a * min_b - a[0] * b[0])

if __name__ == "__main__":
    main()
