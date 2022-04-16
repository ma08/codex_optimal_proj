

def max_triple(x,y,z):
    if x == y and y == z:
        return "YES\n{} {} {}".format(x,y,z)
    elif x != y and x != z and y != z:
        return "NO"
    else:
        return "YES"

def main():
    t = int(input())
    for _ in range(t):
        x,y,z = map(int,input().split())
        print(max_triple(x,y,z))

if __name__ == "__main__":
    main()
