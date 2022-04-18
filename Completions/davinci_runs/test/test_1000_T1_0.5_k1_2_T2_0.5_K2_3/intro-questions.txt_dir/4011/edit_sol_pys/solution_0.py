

def main():
    f = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}

    n = int(input())
    a = input().split()

    for i in range(len(a)):
        a[i] = f[int(a[i])]

    a = ''.join(a)

    a = ''.join(a)

    print(int(a, 16))

if __name__ == '__main__':
    main()
