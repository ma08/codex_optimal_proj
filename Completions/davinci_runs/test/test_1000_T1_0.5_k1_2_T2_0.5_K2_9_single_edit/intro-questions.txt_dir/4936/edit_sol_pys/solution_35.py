

def main():
    days = int(input())
    temp = [int(i) for i in input().split()][:days]
    m = max(temp)
    for i in range(days-2):  # the last two days are not possible
        t = max(temp[i:i+3])
        if t < m:
            m = t
            d = i+1
    print(d, m)

if __name__ == '__main__':
    main()
