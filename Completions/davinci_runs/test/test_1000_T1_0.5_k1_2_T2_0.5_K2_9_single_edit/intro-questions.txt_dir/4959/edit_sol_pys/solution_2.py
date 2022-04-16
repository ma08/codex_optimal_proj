

def main():
    e,f,c = map(int, input().split())
    count = 0
    while e+f >= c:
        count += (e+f)//c
        e,f = (e+f)%c, e+f//c
    print(count)

main()
