

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-1])
 
main()
