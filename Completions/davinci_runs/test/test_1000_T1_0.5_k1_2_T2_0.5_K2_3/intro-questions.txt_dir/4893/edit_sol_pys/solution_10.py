def main():
    n = int(input())
    d = [int(x) for x in input().split()] # list comprehension
    d.sort()
    min_dist = d[0] 
    for i in range(1, n):
        if d[i] - d[i - 1] < min_dist:
            min_dist = d[i] - d[i - 1]
    print(min_dist)



if __name__ == "__main__":
    main()
