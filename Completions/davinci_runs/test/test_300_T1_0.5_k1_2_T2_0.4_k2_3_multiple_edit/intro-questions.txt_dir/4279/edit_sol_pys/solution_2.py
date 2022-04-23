
def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(find(k))

def find(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    if k == 3:
        return 2
    
    num = 0
    start = 3
    end = 6
    while num < k:
        for j in range(start, end + 1):
            num += 1
            if num == k:
                return j
    
    return find(k - num + 1)

if __name__ == '__main__':
    main()
