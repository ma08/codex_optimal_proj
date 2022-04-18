

def main():
    n = int(input())
    a = list(map(int, input().split()))
    day = 1
    for i in range(n):
        if day < a[i]:
            day = a[i]
        day += 1 
    print(day-1) 

if __name__ == '__main__':
    main()
