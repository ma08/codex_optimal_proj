

def main():
    n = int(input())
    s = input().strip()
    t = input().strip()
    res = ''
    for i in range(n):
        res += s[i]
        res += t[i]
    print(res)

if __name__ == '__main__':
    main() 
