

def main():
    #read input
    n = int(input())
    a = list(map(int, input().split()))
    #find unique elements
    unique = []
    for i in range(n-1, -1, -1):
        if a[i] not in unique:
            unique.append(a[i])
    #print results
    print(len(unique), *unique[::-1], sep='\n')
        
if __name__ == '__main__':
    main()
