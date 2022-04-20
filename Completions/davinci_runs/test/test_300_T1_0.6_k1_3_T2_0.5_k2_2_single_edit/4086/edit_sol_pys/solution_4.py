

def main():
    #read input
    n = int(input())
    a = list(map(int, input().split()))[::-1]
    #find unique elements
    unique = []
    for i in range(n):
        if a[i] not in unique:
            unique.append(a[i])
    #print results
    print(len(unique))
    print(*unique)
        
if __name__ == '__main__':
    main()
