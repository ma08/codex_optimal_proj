
#-----main-----
def main():

    n = int(input())
    if n==1:
        print("Hello World")
    elif n==2:
        a,b=map(int,input().split())
        print(a+b)

if __name__ == '__main__':
    main()
