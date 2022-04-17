
def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(find(k, 1))

def find(k, level):
    if k <= level:
        return level
    
    return find(k - level, level + 1)

if __name__ == '__main__':
    main()
