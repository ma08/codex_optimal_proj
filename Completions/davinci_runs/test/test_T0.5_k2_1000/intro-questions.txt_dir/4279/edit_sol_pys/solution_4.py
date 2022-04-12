
def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(find(k, 1))

def find(k, i):
    if k == 1:
        return i
    if k == 2:
        return i
    if k == 3:
        return i + 1
    
    if k <= i * 6:
        return find(k, i)
    else:
        return find(k - i * 6, i + 1)
    

if __name__ == '__main__':
    main()
