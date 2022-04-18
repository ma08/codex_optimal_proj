

def main():
    a, b = [int(x) for x in input().split()]
    if int(str(a)[::-1]) > int(str(b)[::-1]) :
        print(a)
    else:
        print(b)

main() 
