

def main():
    s = input().split()
    t = input().split()
    count = 0
    for i in range(len(s)-1):
        if s[i+1] != t[i+1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
