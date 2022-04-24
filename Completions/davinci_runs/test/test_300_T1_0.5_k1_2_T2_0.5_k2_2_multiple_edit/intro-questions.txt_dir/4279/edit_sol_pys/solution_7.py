
def main():
    q = int(input())  # number of test cases
    for i in range(q):  # loop through test cases
        k = int(input())
        print(find(k))

def find(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    if k == 3:
        return 2
    
    if k <= 6:
        if k == 4:
            return 2
        if k == 5:
            return 3
        return k
    
    return find(k - 6)

if __name__ == '__main__':
    main()
