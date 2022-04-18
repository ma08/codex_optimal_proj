

def main():
    days = int(input())
    temp = [int(i) for i in input().split()]    
    m = max(temp[1:3])
    d = 1
    for i in range(days-2):
        t = max(temp[i:i+3])
        if t < m:
            m = t
            d = i+1
    print(d, m)

if __name__ == '__main__':
    main()
