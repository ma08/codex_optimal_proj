

def Main(k, x):
    if (500 * k) >= x:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    k, x = [int(i) for i in input().split()]
    print(Main(k, x))
