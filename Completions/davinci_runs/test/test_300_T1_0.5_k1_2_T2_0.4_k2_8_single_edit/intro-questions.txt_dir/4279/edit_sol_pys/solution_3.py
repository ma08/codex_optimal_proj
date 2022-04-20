
import math

def main():
    print(find(10))

def find(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    if k == 3:
        return 2
    
    if k == 4:
        return 2
    if k == 5:
        return 3
    if k == 6:
        return 3
    if k == 7:
        return 4
    if k == 8:
        return 4
    if k == 9:
        return 5
    if k == 10:
        return 5
    
    return find(k - 10 + 1)

if __name__ == '__main__':
    main()
