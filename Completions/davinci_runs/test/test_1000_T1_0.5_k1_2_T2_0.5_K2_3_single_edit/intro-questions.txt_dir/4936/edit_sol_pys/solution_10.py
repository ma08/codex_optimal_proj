

def main():
    days = int(input())
    temp = list(map(int, input().split()))
    m = max(temp)
    for i in range(days-2):
        t = max(temp[i:i+3]) 
        if t < m:
            m = t
            d = i+1
    print(d, m)

if __name__ == '__main__':
    main()
