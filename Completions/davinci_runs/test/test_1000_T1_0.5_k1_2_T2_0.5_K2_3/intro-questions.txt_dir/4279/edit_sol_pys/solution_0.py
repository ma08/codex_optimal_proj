
def main():
    t = int(input())
    for i in range(t):
        k = int(input())
        print(find_num(k))

def find_num(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    if num == 3:
        return 2
    
    start = 3
    end = 6
    while end < num:
        end += 9
    
    return find_num(num - start + 1)

if __name__ == '__main__':
    main()
