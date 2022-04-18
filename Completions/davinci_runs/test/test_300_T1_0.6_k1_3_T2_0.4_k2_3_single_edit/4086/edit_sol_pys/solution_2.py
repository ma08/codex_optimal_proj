

def main():
    #read input
    n = int(input("n = "))
    a = list(map(int, input("Enter the array: ").split()))
    #find unique elements
    unique = []
    for i in range(n-1, -1, -1):
        if a[i] not in unique:
            unique.append(a[i])
    #print results
    print(len(unique))
    print(*unique[::-1])
        
if __name__ == '__main__':
    main()
