

def main():
    num = int(input())
    if num == 1:
        print(0)
        return
    print(num*(num-1)//2)

main()
