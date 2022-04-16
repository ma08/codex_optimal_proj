

def max_triple(x,y,z):
    if x == y:
        if y == z:
            return "YES\n"+str(x)+" "+str(y)+" "+str(z)
        else:
            return "NO"
    elif x == z:
        return "NO"
    elif y == z:
        return "NO"
    elif (x > y) and (x > z):
        if y > z:
            return "YES\n"+str(x)+" "+str(y)+" "+str(z)
        else:
            return "YES\n"+str(x)+" "+str(z)+" "+str(y)
    elif (y > x) and (y > z):
        if x > z:
            return "YES\n"+str(y)+" "+str(x)+" "+str(z)
        else:
            return "YES\n"+str(y)+" "+str(z)+" "+str(x)
    elif (z > x) and (z > y):
        if x > y:
            return "YES\n"+str(z)+" "+str(x)+" "+str(y)
        else:
            return "YES\n{} {} {}".format(z,y,x)

def main():
    t = int(input())
    for _ in range(t):
        x,y,z = map(int,input().split())
        print(max_triple(x,y,z))

if __name__ == "__main__":
    main()
