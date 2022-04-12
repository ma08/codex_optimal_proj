

def main():
    n = int(input())
    l = [0, 1]
    for i in range(n):
        l.append(l[i] + l[i+1])
    print(l[n])

if __name__ == '__main__':
    main()
