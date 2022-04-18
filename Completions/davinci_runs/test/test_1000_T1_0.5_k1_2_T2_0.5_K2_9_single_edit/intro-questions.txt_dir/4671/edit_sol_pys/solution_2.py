

def wrapper(f):
    def fun(l1):
        # complete the function
        for i in range(len(l1)):
            if l1[i][0]=="0":
                l1[i]="+91 "+l1[i][1:4]+" "+l1[i][4:]
            elif l1[i][0]=="+":
                l1[i]="+91 "+l1[i][4:9]+" "+l1[i][9:]
            else:
                l1[i]="+91 "+l1[i][0:5]+" "+l1[i][5:]
        return f(l1)
    return fun

@wrapper
    print(*sorted(l1), sep='\n')

if __name__ == '__main__':
    l1 = [input() for _ in range(int(input()))]
    sort_phone(l1)
