

def main():
    a = int(input())
    print(log2(a))

def log2(a):
    return int(math.log(a, 2))

if __name__ == '__main__':
    main()