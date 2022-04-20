

def main():
    #read input
    n = int(input()) #number of elements
    a = list(map(int, input().split())) #list of elements
    #find unique elements
    unique = []
    for i in range(n-1, -1, -1):
        if a[i] not in unique:
            unique.append(a[i])
    #print results
    print(len(unique))
    print(*unique[::-1]) #print elements in reverse order
        
if __name__ == '__main__':
    main()
